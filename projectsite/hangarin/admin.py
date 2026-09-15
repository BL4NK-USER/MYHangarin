from django.contrib import admin
from .models import Category, Task, Priority, Note, SubTask

admin.site.register(Category)
admin.site.register(Task)
admin.site.register(SubTask)
admin.site.register(Priority)
admin.site.register(Note)