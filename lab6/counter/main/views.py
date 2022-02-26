from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Count
from django.db.models import Sum
from django.db.models import F

# Create your views here.
def index(request):
    all_items = Count.objects.all().order_by('id')
    total_count = Count.objects.aggregate(Sum('count'))['count__sum']
    context = {'all_items': all_items, 'total_count': total_count}
    return render(request, "./index.html" , context)

def add_item(request, pk=None):
    item = Count.objects.filter(pk=pk).update(count=F('count')+1)
    return redirect('index')

def remove_item(request, pk=None):
    item = Count.objects.filter(pk=pk).update(count=F('count')-1)
    return redirect('index')
