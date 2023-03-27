from django.urls import reverse, resolve
from django.test import SimpleTestCase
from ..views import CreateNovel, CreateAuthor, CreateTag, detail_view, update_view, delete_view, SignUpView

class TestUrls(SimpleTestCase):
    def test_createNovel_url_is_resolved(self):
        url = reverse('WebNovels:Form')
        self.assertEquals(resolve(url).func.view_class, CreateNovel)

    def test_createAuthor_url_is_resolved(self):

        url = reverse('WebNovels:Form2')
        self.assertEquals(resolve(url).func.view_class, CreateAuthor)

    def test_createTag_url_is_resolved(self):
        url = reverse('WebNovels:Form3')
        self.assertEquals(resolve(url).func.view_class, CreateTag)

    def test_detail_url_is_resolved(self):
        url = reverse('WebNovels:detail', args=['36'])
        self.assertEquals(resolve(url).func, detail_view)

    def test_update_url_is_resolved(self):
        url = reverse('WebNovels:update', args=['36'])
        self.assertEquals(resolve(url).func, update_view)

    def test_delete_url_is_resolved(self):
        url = reverse('WebNovels:delete', args=['36'])
        self.assertEquals(resolve(url).func, delete_view)

    def test_signup_url_is_resolved(self):
        #check if the signup redirect is working correctly
        url = reverse('WebNovels:signup')
        self.assertEquals(resolve(url).func.view_class, SignUpView)