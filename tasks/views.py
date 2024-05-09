from django.shortcuts import render

# Create your views here.

from django.http import JsonResponse
from django.core.serializers import serialize
from .models import task

def index(request):
    tasks=task.objects.all()
    data = serialize('python',tasks)
    
    return JsonResponse(data, safe=False)    
    


