from django.db import models

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add = True, db_index = True)
    updated_at = models.DateTimeField(auto_now = True)

    class Meta:
        abstract = True

class Priority(BaseModel):
    priority_name = models.CharField(max_length = 50)

    class Meta:
            verbose_name = "Priority"
            verbose_name_plural = "Priorities"

    def __str__(self):
        return self.priority_name

class Category(BaseModel):
    category_name = models.CharField(max_length = 50)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.category_name

class Task(BaseModel):
    task_title = models.CharField(max_length = 50)
    description = models.CharField(max_length = 150)
    deadline = models.DateTimeField()
    status = models.CharField(max_length = 50, choices = [("Pending","Pending"),("In Progress","In Progress"),("Completed","Completed")],default = "pending")
    priority = models.ForeignKey(Priority, on_delete = models.CASCADE)
    category = models.ForeignKey(Category, on_delete = models.CASCADE)

    def __str__(self):
        return self.title

class Note(BaseModel):
    task = models.ForeignKey(Task, on_delete = models.CASCADE)
    content = models.TextField(blank = True, null = True)
    
    def __str__(self):
        return self.content

class SubTask(BaseModel):
    subtask_title = models.CharField(max_length = 50)
    status = models.CharField(max_length = 50, choices = [("Pending","Pending"),("In Progress","In Progress"),("Completed","Completed")],default = "pending")
    parent_task = models.ForeignKey(Task, on_delete = models.CASCADE)

    def __str__(self):
        return self.subtask_title


