import json

from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from .models import Score
from rest_framework.reverse import reverse

# Create your tests here.
class ScoreTestCase(TestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(
            username='userA', 
            email='userA@bar.com', 
            password='123456'
        )
        Token.objects.create(user=self.user)
        Score.objects.create(point=100,user=self.user)
        
        self.userB = User.objects.create_user(
            username='userB',
            email='userB@bar.com',
            password='123456'
        )
        self.tokenB = Token.objects.create(user=self.userB)
        
        super(ScoreTestCase, self).setUp()
    
    def test_authorization_success(self):
        response = self.client.get(
            reverse('scores-detail'), 
            {}, 
            HTTP_AUTHORIZATION='Token {}'.format(self.user.auth_token.key)
        )
        self.assertEqual(response.status_code, 200)
    
    def test_authorization_failed(self):
        response = self.client.get(reverse('scores-detail'), {})
        self.assertEqual(response.status_code, 401)
    
    def test_get_score_success(self):
        response = self.client.get(
            reverse('scores-detail'), 
            {}, 
            HTTP_AUTHORIZATION='Token {}'.format(self.user.auth_token.key)
        )
        
        data = json.loads(response.content)
        self.assertEqual(response.status_code, 200)
        assert len(data['result']) >= 1
        
    def test_get_score_failed(self):
        response = self.client.get(
            reverse('scores-detail'), 
            {}, 
            HTTP_AUTHORIZATION='Token {}'.format(self.userB.auth_token.key)
        )
        
        data = json.loads(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(data['result']), 0)