from django.test import TestCase, Client
from django.urls import reverse
from ..models import WebNovels, Author, Tag
class Testviews(TestCase):

    def setUp(self):
        # Every test needs a client.
        self.client = Client()
        self.index_url = reverse('WebNovels:index')
        self.form_url = reverse('WebNovels:Form')
        self.form2_url = reverse('WebNovels:Form2')
        self.form3_url = reverse('WebNovels:Form3')
        self.detail_url = reverse('WebNovels:detail', args=['0905'])
        self.update_url = reverse('WebNovels:update', args=['0905'])
        self.delete_url = reverse('WebNovels:delete', args=['0905'])
        self.signup_url = reverse('WebNovels:signup')
        self.testauthor = Author.objects.create(name='testAuthor', mail='test@test.test')
        self.testtag = Tag.objects.create(name='testTag')
        self.testtag.save()
        self.testwebnovel = WebNovels.objects.create(
            name='test',
            author=self.testauthor,
            status='Completed',
            id='905',
            price=0,
            views=0,
            length=0,
        )

        self.testwebnovel.save()
        self.testwebnovel.tags.add(self.testtag)

    def test_index_GET(self):
        # test if the index page is working
        response = self.client.get(self.index_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'WebNovels/home.html')

    def test_form_GET(self):
        # test if the form page is working
        response = self.client.get(self.form_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'WebNovels/form.html')

    def test_form2_GET(self):
        # test if the form2 page is working
        response = self.client.get(self.form2_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'WebNovels/form2.html')

    def test_form3_GET(self):
        # test if the form3 page is working
        response = self.client.get(self.form3_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'WebNovels/form3.html')

    def test_detail_GET(self):
        # test if the detail page is working
        response = self.client.get(self.detail_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'WebNovels/detail.html')

    def test_update_GET(self):
        # test if the update page is working
        response = self.client.get(self.update_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'WebNovels/update.html')

    def test_delete_GET(self):
        # test if the delete page is working
        response = self.client.get(self.delete_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'WebNovels/delete.html')

    def test_signup_GET(self):
        # test if the signup page is working
        response = self.client.get(self.signup_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/signup.html')
