from django.forms import ModelForm
from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic


class NovelFrom(ModelForm):
    class Meta:
        model = WebNovels
        fields = ['name', 'price', 'author', 'status', 'length', 'tags', 'views']

class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'mail']
class TagForm(ModelForm):
    class Meta:
        model = Tag
        fields = ['name']

class CreateNovel(generic.CreateView):
    form_class = NovelFrom
    model = WebNovels
    template_name = 'WebNovels/form.html'
    success_url = '/webnovels/'
    def form_valid(self, form):
        novel = form.save(commit=False)
        novel.user = self.request.user
        novel.save()
        return super().form_valid(form)

class CreateAuthor(generic.CreateView):
    form_class = AuthorForm
    model = AuthorForm
    template_name = 'WebNovels/form2.html'
    success_url = '/webnovels/form'
    def form_valid(self, form):
        author = form.save(commit=False)
        author.user = self.request.user
        author.save()
        return super().form_valid(form)

class CreateTag(generic.CreateView):
    form_class = TagForm
    model = TagForm
    template_name = 'WebNovels/form3.html'
    success_url = '/webnovels/form'
    def form_valid(self, form):
        tag = form.save(commit=False) # Don't save the tag yet.
        tag.user = self.request.user # Set the user of the tag to the current user
        tag.save()
        return super().form_valid(form) # Call the "real" save() method.


def detail_view(request, id):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # add the dictionary during initialization
    context["data"] = WebNovels.objects.get(id=id)

    return render(request, "WebNovels/detail_view.html", context)


def update_view(request, id):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # fetch the object related to passed id
    obj = get_object_or_404(WebNovels, id=id)

    # pass the object as instance in form
    form = NovelFrom(request.POST or None, instance=obj)

    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/webnovels/" + id)

    # add form dictionary to context
    context["form"] = form
    return render(request, "WebNovels/update_detail.html", context)


def delete_view(request, id):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # fetch the object related to passed id
    obj = get_object_or_404(WebNovels, id=id)

    if request.method == "POST":
        # delete object
        obj.delete()
        # after deleting redirect to
        # home page
        return HttpResponseRedirect("/webnovels/")

    return render(request, "WebNovels/delete_view.html", context)


class Index(generic.ListView):
    model = WebNovels
    template_name = 'WebNovels/home.html'
    context_object_name = "books"

    def get_queryset(self):
        return WebNovels.objects.all()

class SignUpView(generic.CreateView):
    form_class = UserCreationForm # This is the form that will be used to create a new user
    success_url = reverse_lazy("login") # This is the URL that the user will be redirected to after a successful signup
    template_name = "registration/signup.html" # This is the template that will be used to display the signup form
