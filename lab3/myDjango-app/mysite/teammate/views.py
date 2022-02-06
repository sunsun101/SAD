from django.shortcuts import render

from django.http import HttpResponse
from .models import Teammate

def index(request):
    members = list(Teammate.objects.all())
    names = []
    for m in members:
        name = f"{m.id}. {m.title} {m.first_name} {m.last_name}"
        names.append(name)
    return HttpResponse("<br>".join(names))