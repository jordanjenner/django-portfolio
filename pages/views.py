from django.shortcuts import render
from .models import Page, SocialLink

# Create your views here.


def home_view(request, *args, **kwargs):
    pages = Page.objects.order_by('position')
    socials = SocialLink.objects.all()

    context = {
        "pages":    pages,
        "socials":  socials,
    }
    return render(request, "index.html", context)
