from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Task

class TaskTest(APITestCase):  
    
    @classmethod
    def setUpClass(cls):
        user_class = get_user_model()
        cls.user = user_class.objects.create(username="john", password="1234",email="foo@bar.com",bio="nothing")
        
        # Generación del token JWT
        refresh = RefreshToken.for_user(cls.user)
        cls.token = str(refresh.access_token)
        
        cls.task = Task.objects.create(
            name="My Task", description="My task description", user=cls.user
        )
        
    
        
    @classmethod
    def tearDownClass(cls):
         cls.task.delete()
         cls.user.delete()
        

    def setUp(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')    


    def test_get_task_list(self):
        url = reverse("tasks-list")
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        
    def test_get_task_detail(self):
         url=reverse("tasks-detail", kwargs={"pk":self.task.id})
         response= self.client.get(url,format="json")
         self.assertEqual(response.status_code, status.HTTP_200_OK)
         self.assertEqual(response.data.get("name"), self.task.name)
    
       
    def test_create_task(self):
         url = reverse("tasks-list")
         data = {"name": "New Task", "description": "New Task Description", "priority": "8"}
         response = self.client.post(url, data, format="json")
         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
         self.assertEqual(response.data.get("name"), "New Task")
         
    def test_update_task(self):
          url = reverse("tasks-detail", kwargs={"pk": self.task.id})
          data = {"name": "Updated Task", "description": "Updated Task Description", "priority": "9","completed": False}
          response = self.client.put(url, data, format="json")
          self.assertEqual(response.status_code, status.HTTP_200_OK)
          self.assertEqual(response.data.get("name"),"Updated Task")
    
    def test_delete_task(self):
         url = reverse("tasks-detail", kwargs={"pk": self.task.id})
         response = self.client.delete(url, format="json")
         self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
         self.assertFalse(Task.objects.filter(id=self.task.id).exists())  
    
