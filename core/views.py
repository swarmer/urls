from django.shortcuts import redirect, get_object_or_404

from .models import Link


def url(request, short_url):
    link = get_object_or_404(Link, name=short_url)
    return redirect(link.target)
