<<<<<<< Updated upstream
=======

>>>>>>> Stashed changes
from .models import Task
from rest_framework import serializers


<<<<<<< Updated upstream
class TaskSerializer(serializers.HyperlinkedModelSerializer):  
=======
class TaskSerializer(serializers.HyperlinkedModelSerializer):
   
    
>>>>>>> Stashed changes
    class Meta:
        model=Task
        fields=['id','name','description','priority','completed']
        
    def create(self, validated_data):
        validated_data['user']=self.context['request'].user
<<<<<<< Updated upstream
        return super(TaskSerializer,self).create(validated_data)  
    
    
    def destroy(self, validated_data):
        validated_data['user']=self.context['request'].user
        print(validated_data)
        return super(TaskSerializer,self).destroy(validated_data)
=======
        return super(TaskSerializer,self).create(validated_data)  
>>>>>>> Stashed changes
