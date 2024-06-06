from django.shortcuts import render
from .serializers import TaskSerializer
from rest_framework import viewsets
from .models import Task
from rest_framework.filters import OrderingFilter
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class TaskViewSet(viewsets.ModelViewSet):
    
    serializer_class=TaskSerializer 
    filter_backends=[OrderingFilter]
    orderingFilter=['priority'] 

    def get_queryset(self):
        return self.request.user.tasks.all()


    def create(self, request, *args, **kwargs):
        data=request.data
        data["user"]=self.get_serializer(data=data)
        serializer=self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers=self.get_success_headers(serializer.data)
    
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


    def destroy(self, request, *args, **kwargs):
        data=self.get_object()["name"]
        print (data)
        if data["id"] == self.get_serializer(data=data):
            self.serializer_class.destroy()
        return Response(status=status.HTTP_204_NO_CONTENT)


