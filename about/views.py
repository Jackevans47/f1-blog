from django.shortcuts import render
from .models import About

# Create your views here.


def about_me(request):
    """
    Renders the About page with most recent information.
    Displays an individual instance of :model"`about.About`.
    """
    about = About.objects.all().order_by("-updated_on").first()

    return render(
        request,
        "about/about.html",
        {"about": about},
    )
