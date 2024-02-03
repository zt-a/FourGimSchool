from django.shortcuts import render
from .models import BestStudents, AchievementStudents, AchievementPersonal, CompetitiveAchievement


def achievement(request):
    students = BestStudents.objects.filter(is_published=True)[:9]
    achievements_students = AchievementStudents.objects.filter(is_published=True)[:9]
    achievements_personal = AchievementPersonal.objects.filter(is_published=True)[:9]
    achievements = CompetitiveAchievement.objects.filter(is_published=True)[:9]

    context = {
        'best_students': students,
        'achievements_students': achievements_students,
        'achievements_personal': achievements_personal,
        'achievements': achievements,
    }
    return render(request, 'achievement/achievement.html', context)


def best_students(request):
    students = BestStudents.objects.filter(is_published=True)
    return render(request, 'achievement/best_students.html', {'best_students': students})


def achievement_students(request):
    achievements = AchievementStudents.objects.filter(is_published=True)
    return render(request, 'achievement/achievement_students.html', {'achievements_students': achievements})


def achievement_personal(request):
    achievements = AchievementPersonal.objects.filter(is_published=True)
    return render(request, 'achievement/achievement_personal.html', {'achievements_personal': achievements})


def competitive_achievement(request):
    achievements = CompetitiveAchievement.objects.filter(is_published=True)
    return render(request, 'achievement/competitive_achievement.html', {'achievements': achievements})
