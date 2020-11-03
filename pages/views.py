from django.shortcuts import render
from .models import Page, SocialLink
from projects.models import Project
from contact.models import Message
from contact.apps import send_email
from contact.forms import ContactForm
from django.http import HttpResponseRedirect

# Create your views here.


def home_view(request, *args, **kwargs):
    if request.method == "GET":
        pages = Page.objects.filter(show=True).order_by('position')
        socials = SocialLink.objects.all()
        projects = Project.objects.filter(is_private=False).order_by('-last_updated')
        form = ContactForm()

        context = {
            "pages":    pages,
            "socials":  socials,
            "projects": projects,
            "form":     form,
        }

        if request.session.get('submit_success', None) is not None:
            context["success"] = request.session.get('submit_success')
            del request.session['submit_success']

        return render(request, "index.html", context)

    elif request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            request.session['submit_success'] = True
            form.process()
            return HttpResponseRedirect('/#contact')
        else:
            request.session['submit_success'] = False
            return HttpResponseRedirect('/#contact')