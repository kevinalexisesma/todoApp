from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Task

<<<<<<< Updated upstream
admin.site.register(Task)
=======
@admin. register (Task)
class TaskAdmin(admin.ModelAdmin):
    list_display=['id', 'name','description','priority', 'user','completed']
    search_fields=['name']
    
>>>>>>> Stashed changes
