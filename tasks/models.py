from django.db import models

# Create your models here.

class task(models.Model):
    name=models.CharField(max_length=200)
    description=models.TextField()
    
    def __str__(self) -> str:
        texto= "{0} ({1})"
        
        return texto.format(self.name, self.description )