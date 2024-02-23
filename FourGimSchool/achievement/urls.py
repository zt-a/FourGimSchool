from django.urls import path
from .views import *


app_name = 'achievement'

urlpatterns = [
    path('achievements/', achievement, name='achievement'),
    path('best_students/', best_students, name='best_students'),
    path('achievement_students/', achievement_students, name='achievement_students'),
    path('achievement_personal/', achievement_personal, name='achievement_personal'),
    path('competitive_achievement/', competitive_achievement, name='competitive_achievement'),
]
