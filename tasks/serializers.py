from .models import Task
from rest_framework import serializers


class TaskSerializer(serializers.HyperlinkedModelSerializer):
   
    
    class Meta:
        model=Task
        fields=['id','name','description','priority','completed']
        
    def create(self, validated_data):
        validated_data['user']=self.context['request'].user
        return super(TaskSerializer,self).create(validated_data)  
    
    def destroy(self, validated_data):
        instance = Task.objects.get(pk=validated_data.id)
        instance.delete()
        return validated_data
    
    def update(self, validated_data):
        instance = self.get_object()
        id=self.get_object().id
        for field, value in validated_data.items():
            setattr(instance, field, value)
        instance.save()
        return validated_data