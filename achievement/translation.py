from modeltranslation.translator import translator, TranslationOptions
from .models import *


class AchievementStudentsTranslationOptions(TranslationOptions):
    fields = ('description',)


class AchievementPersonalTranslationOptions(TranslationOptions):
    fields = ('description',)


class CompetitiveAchievementTranslationOptions(TranslationOptions):
    fields = ('description',)


translator.register(AchievementPersonal, AchievementPersonalTranslationOptions)
translator.register(AchievementStudents, AchievementStudentsTranslationOptions)
translator.register(CompetitiveAchievement, CompetitiveAchievementTranslationOptions)
