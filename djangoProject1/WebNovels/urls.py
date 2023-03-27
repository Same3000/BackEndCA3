from django.urls import include, path
from .views import SignUpView


from . import views
app_name = 'WebNovels'
urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('form', views.CreateNovel.as_view(), name='Form'),
    path('form2', views.CreateAuthor.as_view(), name='Form2'),
    path('form3', views.CreateTag.as_view(), name='Form3'),
    path('<id>', views.detail_view, name='detail'),
    path('<id>/update', views.update_view, name='update'),
    path('<id>/delete', views.delete_view, name='delete'),
    path("signup/", SignUpView.as_view(), name="signup"),

]
