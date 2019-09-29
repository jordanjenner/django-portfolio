from django.shortcuts import render
from .models import Page, SocialLink
from projects.models import Project

# Create your views here.


def home_view(request, *args, **kwargs):
    pages = Page.objects.order_by('position')
    socials = SocialLink.objects.all()

    context = {
        "pages":    pages,
        "socials":  socials,
    }
    return render(request, "index.html", context)

def projects_view(request, *args, **kwargs):
    pages = Page.objects.order_by('position')
    projects = Project.objects.order_by('-last_updated')

    context = {
        "pages":    pages,
        "projects": projects,
    }

    return render(request, "projects.html", context)

def about_view(request, *args, **kwargs):
    pages = Page.objects.order_by('position')

    context = {
        "pages":    pages,
    }

    return render(request, "about.html", context)

def contact_view(request, *args, **kwargs):
    if request.method == "GET":
        pages = Page.objects.order_by('position')

        context = {
            "pages":    pages,
        }

        return render(request, "contact.html", context)
