from django.test import TestCase
from django.contrib.auth.models import User

from .models import Snippet, Tag


class SnippetTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Creating User
        test_user = User.objects.create_user(
            username='testuser', password='testpassword'
        )
        test_user.save()

        # Creating Tag
        test_tag = Tag.objects.create(title='testtag')
        test_tag.save()

        # Creating Snippet
        test_snippet = Snippet.objects.create( 
            title='Snippet title', content='Snippet content',
            created_user=test_user, tag=test_tag,
        )
        test_snippet.save()

    def test_snippet_content(self):
        snippet = Snippet.objects.get(id=1)

        title = f'{snippet.title}'
        content = f'{snippet.content}'
        created_user = f'{snippet.created_user}'
        tag = f'{snippet.tag}'

        self.assertEqual(title, 'Snippet title')
        self.assertEqual(content, 'Snippet content')
        self.assertEqual(created_user, 'testuser')
        self.assertEqual(tag, 'testtag')