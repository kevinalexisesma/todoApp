
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
    ordering = ['-priority']
   
    
    def get_queryset(self): 
         
        queryset = self.request.user.tasks.all()
        completed = self.request.query_params.get('completed', None)
        
        if completed is not None:
            completed = completed.lower() in ['true', '1', 't', 'y', 'yes']
            queryset = queryset.filter(completed=completed)
        
        return queryset

    def create(self, request, *args, **kwargs):
        data=request.data
        data["user"]=self.get_serializer(data=data)
        serializer=self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers=self.get_success_headers(serializer.data)
    
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def destroy(self, request, *args, **kwargs):
        data=self.get_object()
        self.serializer_class.destroy(self,validated_data=data)
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def update(self, request, *args, **kwargs):
        data=request.data
        self.serializer_class.update(self,validated_data=data)
        return Response(status=status.HTTP_200_OK)
