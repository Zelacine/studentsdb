from django.contrib import admin
from .models.students import Student
from .models.groups import Group
from .models.examinations import Examination

# Register your models here.
admin.site.register(Student)
admin.site.register(Group)
admin.site.register(Examination)