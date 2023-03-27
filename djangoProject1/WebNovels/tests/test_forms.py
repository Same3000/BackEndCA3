from django.test import TestCase

from ..views import NovelFrom, AuthorForm, TagForm
from ..models import WebNovels, Author, Tag


class TestFormWebNovels(TestCase):
    def test_empty_form(self):
        form = NovelFrom()
        self.assertIn("name", form.fields)
        self.assertIn("price", form.fields)
        self.assertIn("author", form.fields)
        self.assertIn("status", form.fields)
        self.assertIn("length", form.fields)
        self.assertIn("tags", form.fields)
        self.assertIn("views", form.fields)

    def testform(self):
        # Positive test
        self.testtag = Tag.objects.create(name='testTag')
        self.testtag.save()
        self.testauthor = Author.objects.create(name='testAuthor',  mail='test@test.test')
        self.testauthor.save()
        form_data = {'name': 'test', 'price': 1, 'author': self.testauthor, 'status': 'Completed', 'length': 1,
                     'tags': self.testtag, 'views': 1}
        form = NovelFrom(data=form_data)
        self.assertTrue(form.is_valid())

        # Negative test
        self.testtag = Tag.objects.create(name='testTag')
        self.testtag.save()
        self.testauthor = Author.objects.create(name='testAuthor', mail='test@test.test')
        self.testauthor.save()
        form_data = {'name': 'test', 'price': 1, 'author': self.testauthor, 'status': 'IDK', 'length': 1,
                     'tags': self.testtag, 'views': 1}
        form = NovelFrom(data=form_data)
        # This test is for wrong input since IDK is not a valid status
        self.assertFalse(form.is_valid())



class TestFormAuthor(TestCase):
    def test_empty_form(self):
        form = AuthorForm()
        self.assertIn("name", form.fields)
        self.assertIn("mail", form.fields)

    def testForm(self):
        # Positive test
        form_data = {'name': 'test', 'mail': 'test@test.test'}
        form = AuthorForm(data=form_data)
        self.assertTrue(form.is_valid())

        # Negative test
        form_data = {'name': 'test', 'mail': 'test.test'}
        form = AuthorForm(data=form_data)
        self.assertFalse(form.is_valid())

class TestFormTag(TestCase):
    def test_empty_form(self):
        form = TagForm()
        self.assertIn("name", form.fields)
    def testForm(self):
        # Positive test
        form_data = {'name': 'test'}
        form = TagForm(data=form_data)
        self.assertTrue(form.is_valid())

        # Negative test
        form_data = {'name': None}
        form = TagForm(data=form_data)
        self.assertFalse(form.is_valid())
