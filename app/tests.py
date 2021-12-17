import django
from django.test import TestCase

class AppViewTest(TestCase):
    if django.VERSION[:2] >= (1, 7):
        # Django 1.7 requires an explicit setup() when running tests in PTVS
        @classmethod
        def setUpClass(cls):
            super(AppViewTest, cls).setUpClass()
            django.setup()

    
    def test_index(self):
        """Tests the home page."""
        response = self.client.get('/')
        self.assertContains(response, 'Home Page', 1, 200)




