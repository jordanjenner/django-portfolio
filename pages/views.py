from django.shortcuts import render
from .models import Page

# Create your views here.


def home_view(request, *args, **kwargs):
    pages = Page.objects.order_by('position')
    print(pages)

    context = {
        "pages":    pages
    }
    return render(request, "index.html", context)
