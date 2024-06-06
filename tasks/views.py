
from .serializers import TaskSerializer
from rest_framework import viewsets
from .models import Task
from rest_framework.filters import OrderingFilter
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.exceptions import PermissionDenied, NotFound

# Create your views here.

class TaskViewSet(viewsets.ModelViewSet):
    
    queryset=Task.objects.all()
    authentication_classes=[JWTAuthentication]
    serializer_class=TaskSerializer 
    filter_backends=[OrderingFilter]
    ordering_fields=['name']
    ordering = ['priority','name'] 
    
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

        

