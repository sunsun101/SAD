from django.shortcuts import render

from django.http import HttpResponse
from teammate.models import Teammate
from django.template import loader

def index(request):
    template = loader.get_template("./index.html")
    return HttpResponse(template.render())

def setInterval(request):
    template = loader.get_template("./interval/index.html")
    return HttpResponse(template.render())

def button(request):
    template = loader.get_template("./button/index.html")
    return HttpResponse(template.render())

def assignment(request):
    members = list(Teammate.objects.all())
    names = []
    for m in members:
        name = f"{m.id}. {m.title} {m.first_name} {m.last_name}"
        names.append(name)
    teammates = '\n'.join(names)
    context = {'teammates': teammates}
    return render(request, './button/assignment.html', context)