from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
<<<<<<< Updated upstream
from rest_framework.authtoken.models import Token
=======
from rest_framework_simplejwt.tokens import RefreshToken
>>>>>>> Stashed changes
from .models import Task

class TaskTest(APITestCase):  
    
    @classmethod
    def setUpClass(cls):
        user_class = get_user_model()
        cls.user = user_class.objects.create(username="john", password="1234",email="foo@bar.com",bio="nothing")
<<<<<<< Updated upstream
        cls.token.objects.create(user=cls.user)
=======
        
        # Generación del token JWT
        refresh = RefreshToken.for_user(cls.user)
        cls.token = str(refresh.access_token)
        
>>>>>>> Stashed changes
        cls.task = Task.objects.create(
            name="My Task", description="My task description", user=cls.user
        )
        
    @classmethod
    def tearDownClass(cls):
        cls.task.delete()
        cls.token.delete()
        cls.user.delete()

    def setUp(self):
        self.client.force_authenticate(user=self.user, token=self.token)


    def test_get_task_list(self):
        url=reverse("task-list")
        response=self.client.get(url,format="json")
        self.assertequal(response.status_code, status.HTTP_200_OK)
        self.asserequal(len(response.data.get("results")),1)
        
    def test_get_task_detail(self):
        url=reverse("task-detail", kwargs={"pk":self.task.id})
        response= self.client.get(url,format="json")
        self.assertequal(response.status_code, status.HTTP_200_OK)
<<<<<<< Updated upstream
        self.asserequal(len(response.data.get("name")),self.task.name)
=======
        self.asserequal(len(response.data.get("name")),self.task.name) 
    
>>>>>>> Stashed changes
