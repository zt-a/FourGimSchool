from django.shortcuts import render, get_object_or_404
from .models import *


def personal(request):
    authorities = Authorities.objects.filter(is_published=True)[:3].select_related('person').prefetch_related('person__subjects_taught')
    teachers = Teachers.objects.filter(is_published=True)[:3].select_related('person').prefetch_related('person__subjects_taught')
    parliament = Parliament.objects.filter(is_published=True)[:3].select_related('person')
    retired = RetiredTeachers.objects.filter(is_published=True)[:3].select_related('person').prefetch_related('person__subjects_taught')
    context = {
        'title': 'Персонал',
        'authorities': authorities,
        'teachers': teachers,
        'parliaments': parliament,
        'retireds': retired,
    }
    return render(request, 'personal/personal.html', context)


def all_personal(request):
    personals = PersonalModel.objects.only('profile_picture', 'first_name', 'last_name', 'subjects_taught').filter(is_published=True)
    context = {
        'title': 'Все сотрудники',
        'personals': personals,
    }
    return render(request, 'personal/all_personal.html', context)


def classes(request):
    Classes = ClassModel.objects.only('classroom_number', 'slug', 'pk', 'class_name', 'class_teacher').filter(is_published=True)
    context = {
        'title': 'Классы',
        'classes': Classes
    }
    return render(request, 'personal/class.html', context)


def class_detail(request, slug):
    Class = get_object_or_404(ClassModel, slug=slug, is_published=True)
    context = {
        'title': f'Класс {Class.class_name}',
        'class': Class,
    }
    return render(request, 'personal/class_detail.html', context=context)


def grades_list(request):
    grades = GradesStudents.objects.only('subject', 'student', 'grade', 'quarter').filter(is_published=True)
    context = {
        'title': 'Оценки',
        'grades': grades,
    }
    return render(request, 'personal/grades_list.html', context)