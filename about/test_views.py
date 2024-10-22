from django.test import TestCase
from django.urls import reverse
from .models import About


class AboutMeViewTests(TestCase):
    def setUp(self):
        self.about_instance = About.objects.create(
            title="about/about.html",
            content="about",
        )

    def test_about_me_view_status_code(self):
        response = self.client.get(reverse("about"))
        self.assertEqual(response.status_code, 200)

    def test_about_me_view_template(self):
        response = self.client.get(reverse("about"))
        self.assertTemplateUsed(response, "about/about.html")

    def test_about_me_view_context(self):
        response = self.client.get(reverse("about"))
        self.assertEqual(response.context["about"], self.about_instance)

    def test_about_me_view_contains_correct_html(self):
        response = self.client.get(reverse("about"))
        self.assertContains(response, "about/about.html")
        self.assertContains(response, "about")
