# from django.test import TestCase
from django.test import SimpleTestCase
from django.urls import reverse


# Create your tests here.


class HomePageTests(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):
        response = self.client.get(reverse("home"))
        self.assertTemplateUsed(response, 'testing/home.html')

    def test_template_content(self):
        response = self.client.get(reverse("home"))
        self.assertContains(response, '<h1 class="text-center">Welcome to Home Page</h1>')
        self.assertNotContains(response, "Not on the Page")


class AboutPageTests(SimpleTestCase):  # new
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/about/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):
        response = self.client.get(reverse("about"))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):
        response = self.client.get(reverse("about"))
        self.assertTemplateUsed(response, "testing/about.html")

    def test_template_content(self):
        response = self.client.get(reverse("about"))
        self.assertContains(response, '<h1 class="text-center">Welcome to About Us Page</h1>')
        self.assertNotContains(response, "Should not be here!")
