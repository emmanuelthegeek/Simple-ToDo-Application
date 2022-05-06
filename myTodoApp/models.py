from django.db import models
from django.utils import timezone

# Create your models here.
class Category(models.Model): 
    type = models.CharField(max_length=100) 
    class Meta:
        verbose_name = ("Category")
        verbose_name_plural = ("Categories")
    def __str__(self):
        return self.type

class TodoData(models.Model): 
    name_of_task = models.CharField(max_length=250)
    task = models.TextField(blank=True) 
    date_started = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))
    due_date = models.DateField(default=timezone.now().strftime("%Y-%m-%d")) 
    category = models.ForeignKey(Category, default="personal", on_delete=models.CASCADE,) 
    class Meta:
        ordering = ["-date_started"] 
    def __str__(self):
        return self.name_of_task 