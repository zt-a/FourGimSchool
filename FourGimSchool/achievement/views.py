
from django.shortcuts import render
from .models import BestStudents, AchievementStudents, AchievementPersonal, CompetitiveAchievement


def achievement(request):
    students = BestStudents.objects.filter(is_published=True)[:9]
    achievements_students = AchievementStudents.objects.filter(is_published=True)[:9]
    achievements_personal = AchievementPersonal.objects.filter(is_published=True)[:9]
    achievements = CompetitiveAchievement.objects.filter(is_published=True)[:9]

    context = {
        'title': 'Достижении',
        'best_students': students,
        'achievements_students': achievements_students,
        'achievements_personal': achievements_personal,
        'achievements': achievements,
    }
    return render(request, 'achievement/achievement.html', context)


def best_students(request):
    students = BestStudents.objects.filter(is_published=True)
    return render(request, 'achievement/best_students.html', {'best_students': students, 'title': 'Лучшие ученики',})


def achievement_students(request):
    achievements = AchievementStudents.objects.filter(is_published=True)
    context = {
        'achievements_students': achievements,
        'title': 'Достижении учеников',
    }
    return render(request, 'achievement/achievement_students.html', context)


def achievement_personal(request):
    achievements = AchievementPersonal.objects.filter(is_published=True)
    context = {
        'achievements_personal': achievements,
        'title': 'Достижении учителей',
    }
    return render(request, 'achievement/achievement_personal.html', context)


def competitive_achievement(request):
    achievements = CompetitiveAchievement.objects.filter(is_published=True)
    context = {
        'achievements': achievements,
        'title': 'Соревновательные достижении'
    }
    return render(request, 'achievement/competitive_achievement.html', context)
