from django.contrib import admin
from .models import *


admin.site.register(PersonalModel)
admin.site.register(ClassModel)
admin.site.register(SubjectModel)
admin.site.register(SchedulesModel)