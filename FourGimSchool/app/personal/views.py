from django.shortcuts import render, get_object_or_404
from .models import *


def personal(request):
    return render(request, 'personal/personal.html')


def all_personal(request):
    return render(request, 'personal/all_personal.html')


def classes(request):
    Classes = ClassModel.objects.all()
    context = {
        'classes': Classes
    }
    return render(request, 'personal/class.html', context)


def class_detail(request, slug):
    Class = get_object_or_404(ClassModel, slug=slug)
    context = {
        'class': Class,
    }
    return render(request, 'personal/class_detail.html', context=context)