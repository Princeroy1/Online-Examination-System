from django.contrib import admin

from exam.models import Course,Question,Result

# Register your models here.

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    pass
@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    pass
@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    pass