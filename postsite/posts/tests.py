from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from .models import Post

class PostViewSetTestCase(APITestCase):
    
    def setUp(self):
        # 테스트용 사용자 생성
        self.user = User.objects.create_user(username="testuser", password="testpassword")
        
        # 클라이언트 인스턴스 생성
        self.client = APIClient()

        # 테스트용 게시물 생성
        self.post:Post = Post.objects.create(content="Test Content", writer=self.user)
        
        # URL 세팅
        self.url = "/api/post/"

    def test_create_post(self):
        self.client.login(username="testuser", password="testpassword")
        response = self.client.post(self.url, {"title": "New Post", "content": "New Content"})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_post(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_detail_post(self):
        self.client.login(username="testuser", password="testpassword")
        response = self.client.get(f"{self.url}{self.post.pk}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_post(self):
        self.client.login(username="testuser", password="testpassword")
        response = self.client.put(f"{self.url}{self.post.pk}/", {"title": "Updated", "content": "Updated Content"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_delete_post(self):
        self.client.login(username="testuser", password="testpassword")
        response = self.client.delete(f"{self.url}{self.post.pk}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)