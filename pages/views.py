from django.shortcuts import render
from .models import Page, SocialLink
from projects.models import Project
from contact.models import Message
from contact.apps import send_email
from contact.forms import ContactForm
from django.http import HttpResponseRedirect

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
    projects = Project.objects.filter(is_private=False).order_by('-last_updated')

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
        form = ContactForm()

        context = {
            "success":  request.session.get('submit_success', None),
            "pages":    pages,
            "form":     form,
        }

        if request.session.get('submit_success', None) is not None:
            del request.session['submit_success']

        return render(request, "contact.html", context)

    elif request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            request.session['submit_success'] = True
            form.process()
            return HttpResponseRedirect('/contact/')
        else:
            request.session['submit_success'] = False
            return HttpResponseRedirect('/contact/')
            
            

