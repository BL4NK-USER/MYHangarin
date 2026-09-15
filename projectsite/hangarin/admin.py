from django.contrib import admin
from .models import Category, Task, Priority, Note, SubTask

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("category_name",)
    search_fields = ("category_name",)

@admin.register(Priority)
class PriorityAdmin(admin.ModelAdmin):
    list_display = ("priority_name",)
    search_fields = ("priority_name",)

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("task_title", "status", "deadline", "priority", "category")
    search_fields = ("task_title","description",)
    list_filter = ("status","priority","category")

@admin.register(SubTask)
class SubTaskAdmin(admin.ModelAdmin):
    list_display = ("subtask_title","status","parent_task_name")
    search_fields = ("subtask_title",)
    list_filter = ("status",)

    def parent_task_name(self, obj):
        return obj.parent_task.task_title

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ("task","content","created_at")
    search_fields = ("content",)
    list_filter = ("created_at",)
