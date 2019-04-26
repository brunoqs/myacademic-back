from django.contrib import admin

from .models import Class, ClassContent


@admin.register(Class)
class ClassAdmin(admin.ModelAdmin):
    pass


@admin.register(ClassContent)
class ClassContentAdmin(admin.ModelAdmin):
    pass
