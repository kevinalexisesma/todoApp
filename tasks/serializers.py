from .models import Task
from rest_framework import serializers


class TaskSerializer(serializers.HyperlinkedModelSerializer):
   
    
    class Meta:
        model=Task
        fields=['id','name','description','priority','completed']
        
    def create(self, validated_data):
        validated_data['user']=self.context['request'].user
        return super(TaskSerializer,self).create(validated_data)  
