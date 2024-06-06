<<<<<<< Updated upstream
from django.contrib import admin
from .models import Profile
# Register your models here.

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass
=======
from django. contrib import admin
from profiles.models import Profile
from django.contrib.auth.admin import UserAdmin


@admin.register(Profile)
class ProfileAdmin (UserAdmin):
   list_display=["id","first_name","last_name","username","email","is_superuser"]
   
   search_fields=["username"]
   
>>>>>>> Stashed changes
