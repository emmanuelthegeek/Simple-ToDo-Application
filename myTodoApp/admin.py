from django.contrib import admin
from . import models


class CategoryAdmin(admin.ModelAdmin):
    ViewType = ("type",)
class TodoDataAdmin(admin.ModelAdmin):
    ViewTasks = ("name_of_task",  "date_started", "due_date")
admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.TodoData, TodoDataAdmin)
