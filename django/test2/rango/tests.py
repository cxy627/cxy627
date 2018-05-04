from django.test import TestCase

from django.shortcuts import reverse

from django.contrib.staticfiles import finders

from .models import Category, Page
# Create your tests here.


def add_cat(name, views, likes):
    c = Category.objects.get_or_create(name=name)[0]
    c.views = views
    c.likes = likes
    c.save()
    return c


class CategoryMethodTests(TestCase):

    def setUp(self):
        try:
            from .populate_rango import populate
            populate()
        except ImportError:
            print('The module populate_rango does not exist')
        except NameError:
            print('The function populate() does not exist or is not correct')
        except:
            print('Something went wrong in the populate() function :-(')

    def get_category(self, name):
        from .models import Category
        try:
            cat = Category.objects.get(name=name)
        except Category.DoesNotExist:
            cat = None
        return cat

    def test_python_cat_added(self):
        cat = self.get_category('Python')
        self.assertIsNotNone(cat)

    def test_python_cat_with_views(self):
        cat = self.get_category('Python')
        self.assertEquals(cat.views, 128)

    def test_python_cat_with_likes(self):
        cat = self.get_category('Python')
        self.assertEquals(cat.likes, 64)

    def test_python_slug_crearion(self):
        cat = Category(name="Random Category String", views=1, likes=1)
        cat.save()
        self.assertEqual(cat.slug, "random-category-string")

    # Need to add tests to:

    # check admin interface - is it configured and set up


class IndexViewTests(TestCase):

    def test_index_view_with_no_categories(self):
        response = self.client.get(reverse("rango:index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "暂无类型")
        self.assertQuerysetEqual(response.context["categories"], [])

    def test_index_view_with_categories(self):

        add_cat("test", 1, 1)
        add_cat("temp", 1, 1)
        add_cat("tmp", 1, 1)
        add_cat("tmp test temp", 1, 1)

        response = self.client.get(reverse("rango:index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "tmp test temp")

        num_cats = len(response.context["categories"])
        self.assertEqual(num_cats, 4)
