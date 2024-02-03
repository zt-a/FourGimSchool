from django.shortcuts import render, get_object_or_404
from .models import *


def personal(request):
    authorities = Authorities.objects.filter(is_published=True)[:3]
    teachers = Teachers.objects.filter(is_published=True)[:3]
    parliament = Parliament.objects.filter(is_published=True)[:3]
    retired = RetiredTeachers.objects.filter(is_published=True)[:3]
    context = {
        'authorities': authorities,
        'teachers': teachers,
        'parliaments': parliament,
        'retireds': retired,
    }
    return render(request, 'personal/personal.html', context)


def all_personal(request):
    personals = PersonalModel.objects.filter(is_published=True)
    context = {
        'personals': personals,
    }
    return render(request, 'personal/all_personal.html', context)


def classes(request):
    Classes = ClassModel.objects.filter(is_published=True)
    context = {
        'classes': Classes
    }
    return render(request, 'personal/class.html', context)


def class_detail(request, slug):
    Class = get_object_or_404(ClassModel, slug=slug, is_published=True)
    context = {
        'class': Class,
    }
    return render(request, 'personal/class_detail.html', context=context)


def grades_list(request):
    grades = GradesStudents.objects.filter(is_published=True)
    context = {
        'grades': grades,
    }
    return render(request, 'personal/grades_list.html', context)