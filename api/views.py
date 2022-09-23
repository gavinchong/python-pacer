from importlib.resources import contents
from multiprocessing import context
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework import permissions
from rest_framework.authentication import TokenAuthentication
from django.http import JsonResponse
from .serializers import ScoreSerializer
from .models import Score
from django.shortcuts import get_object_or_404

class ScoreViewSet(viewsets.ModelViewSet):
    queryset = Score.objects.all()
    serializer_class = ScoreSerializer
    authentication_classes = (TokenAuthentication,)

    def retrieve(self, request):
        user = request.user
        queryset = Score.objects.filter(user_id=user.id)
        score = get_object_or_404(queryset)
        serializer = ScoreSerializer(score)
        return JsonResponse({
                'status': 'success',
                'result': serializer.data
            },
            safe=False
        )