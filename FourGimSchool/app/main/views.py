from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from django.shortcuts import render
from django.db.models import Q
from .models import *
from news.models import News
from personal.models import *


# def search(request):
#     query = request.GET.get('q', '')
#
#     # Поиск в Model1
#     results_model1 = .objects.filter(
#         Q(field1__icontains=query) | Q(field2__icontains=query)
#     )
#
#     # Поиск в Model2
#     results_model2 = Model2.objects.filter(
#         Q(field3__icontains=query) | Q(field4__icontains=query)
#     )
#
#     # Поиск в Model3
#     results_model3 = Model3.objects.filter(
#         Q(field5__icontains=query) | Q(field6__icontains=query)
#     )
#
#     context = {
#         'query': query,
#         'results_model1': results_model1,
#         'results_model2': results_model2,
#         'results_model3': results_model3,
#     }
#
#     return render(request, 'main/search_results.html', context)


def index(request):
    feedback_form = FeedbackForm()
    rules = RulesModel.objects.filter(is_published=True)[:3]
    news = News.objects.filter(is_published=True)[:2]
    authorities = Authorities.objects.filter(is_published=True)[:3]
    teachers = Teachers.objects.filter(is_published=True)[:3]
    parliament = Parliament.objects.filter(is_published=True)[:3]
    retired = RetiredTeachers.objects.filter(is_published=True)[:3]
    context = {

    }

    if feedback_form.is_valid():
        feedback_form.save()
    search_form = SearchForm()

    context = {
        'title': 'Школа №4 Баткен',
        'feedback_form': feedback_form,
        'search_form': search_form,
        'rules': rules,
        'news': news,
        'authorities': authorities,
        'teachers': teachers,
        'parliaments': parliament,
        'retireds': retired,
    }
    return render(request, 'main/index.html', context)


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
    else:
        form = ContactForm()
    if form.is_valid():
        form.save()
        redirect('home')

    context = {
        'title': 'Обратная связь',
        'form': form,
    }
    return render(request, 'main/contact.html', context)


def about(request):
    return render(request, 'main/about.html', {'title': 'О нас'})


def rules(request):
    rules = RulesModel.objects.filter(is_published=True)
    context = {
        'title': 'Правило',
        'rules': rules
    }
    return render(request, 'main/rules.html', context)


def detail_rules(request, slug):
    rule = get_object_or_404(RulesModel, slug=slug, is_published=True)
    prev_rule = RulesModel.objects.filter(number_rule=rule.number_rule - 1).first()
    next_rule = RulesModel.objects.filter(number_rule=rule.number_rule + 1).first()

    context = {
        'title': f'Правило №{rule.pk}',
        'rule': rule,
        'next_rule': next_rule,
        'prev_rule': prev_rule,
    }
    return render(request, 'main/detail_rules.html', context)


def add_feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main:feedback')
    else:
        # Если запрос не метода POST, создаем пустую форму
        form = FeedbackForm()

    return render(request, 'main/add_feedback.html', {'form': form, 'title': 'Оставить отзыв'})


def feedback_list(request):
    feedbacks = FeedbackModel.objects.filter(is_published=True).order_by('-time_create')

    return render(request, 'main/feedback_list.html', {'feedbacks': feedbacks, 'title': 'Отзыв'})
