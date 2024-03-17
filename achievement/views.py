
from django.shortcuts import render
from .models import BestStudents, AchievementStudents, AchievementPersonal, CompetitiveAchievement


def achievement(request):
    students = BestStudents.objects.select_related('class_student').filter(is_published=True)[:9].only('full_name',
                                                                                                       'class_student__class_name',
                                                                                                       'image_student')
    achievements_students = AchievementStudents.objects.filter(is_published=True)[
                            :9].only('full_name', 'image_student', 'description')
    achievements_personal = AchievementPersonal.objects.select_related('personal').filter(is_published=True)[:9].only(
        'personal__first_name', 'personal__last_name', 'personal__patronymic', 'image_personal', 'description')
    achievements = CompetitiveAchievement.objects.filter(is_published=True)[:9].only(
        'full_name', 'image_student', 'description')

    context = {
        'title': 'Достижении',
        'best_students': students,
        'achievements_students': achievements_students,
        'achievements_personal': achievements_personal,
        'achievements': achievements,
    }
    return render(request, 'achievement/achievement.html', context)


def best_students(request):
    students = BestStudents.objects.select_related('class_student').filter(is_published=True)[:9].only('full_name', 'class_student__class_name', 'image_student')
    return render(request, 'achievement/best_students.html', {'best_students': students, 'title': 'Лучшие ученики',})


def achievement_students(request):
    achievements = AchievementStudents.objects.filter(is_published=True)[:9].only('full_name', 'image_student', 'description')
    context = {
        'achievements_students': achievements,
        'title': 'Достижении учеников',
    }
    return render(request, 'achievement/achievement_students.html', context)


def achievement_personal(request):
    achievements = AchievementPersonal.objects.select_related('personal').filter(is_published=True)[:9].only('description', 'image_personal', 'personal__first_name', 'personal__last_name', 'personal__patronymic')
    context = {
        'achievements_personal': achievements,
        'title': 'Достижении учителей',
    }
    return render(request, 'achievement/achievement_personal.html', context)


def competitive_achievement(request):
    achievements = CompetitiveAchievement.objects.only('image_student', 'full_name', 'description').filter(is_published=True)
    context = {
        'achievements': achievements,
        'title': 'Соревновательные достижении'
    }
    return render(request, 'achievement/competitive_achievement.html', context)
