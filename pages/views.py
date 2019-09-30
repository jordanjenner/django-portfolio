from django.shortcuts import render
from .models import Page, SocialLink
from projects.models import Project
from contact.models import Message
from contact.apps import send_email

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
    pages = Page.objects.order_by('position')

    context = {
        "pages":    pages,
    }
    if request.method == "GET":

        return render(request, "contact.html", context)

    elif request.method == "POST":
        email = request.POST.get('email')
        message = request.POST.get('message')
        if email is not None and message is not None:
            message = Message.objects.create(
                email=email,
                message=message)

            send_email(message.email, message.message, message.date_time)

            return render(request, "contact.html", context)
            

