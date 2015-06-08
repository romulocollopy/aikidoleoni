from django.test import TestCase
from model_mommy import mommy
from ckeditor.fields import RichTextField

from aikidoleoni.blog.models import Post


class TestModels(TestCase):

    def test_post_is_created(self):
        mommy.make(Post, id=43)
        post = Post.objects.get()
        self.assertEqual(43, post.id)

    # def test_content_is_RichTextField(self):
    #     post = mommy.make(Post)
    #     self.assertIsInstance(RichTextField, type(Post.content))
