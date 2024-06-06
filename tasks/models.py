from django.db import models
from django.conf import settings

# Create your models here.

class Task(models.Model):
    name=models.CharField(max_length=200)
    description=models.TextField()
    priority=models.PositiveSmallIntegerField(default=0)   
    completed=models.BooleanField(default=False)
    user=models.ForeignKey( 
<<<<<<< Updated upstream
       settings.AUTH_USER_MODEL,
       on_delete=models.RESTRICT,
       limit_choices_to={'is_superuser':False},
       related_name='task',
       null=True
    )
=======
        settings.AUTH_USER_MODEL,
       on_delete=models.RESTRICT,
       limit_choices_to={'is_superuser':False},
       related_name='tasks',
       null=True
    )
    completed=models.BooleanField(default=False)
>>>>>>> Stashed changes
   
    def __str__(self) -> str:
        texto= "{0} ({1})"
        return texto.format(self.name, self.description )