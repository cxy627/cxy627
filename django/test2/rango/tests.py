from django.test import TestCase

from django.shortcuts import reverse

from django.contrib.staticfiles import finders
# Create your tests here.

class Chapter5ViewTests(TestCase):



    def setUp(self):

        try:

            from populate_rango import populate

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



    def test_view_has_title(self):

        response = self.client.get(reverse('index'))



        #Check title used correctly

        self.assertIn('<title>', response.content)

        self.assertIn('</title>', response.content)



    # Need to add tests to:

    # check admin interface - is it configured and set up



    def test_admin_interface_page_view(self):

        from admin import PageAdmin

        self.assertIn('category', PageAdmin.list_display)

        self.assertIn('url', PageAdmin.list_display)
