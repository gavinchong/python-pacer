from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from django.http import JsonResponse
from .serializers import ScoreSerializer
from .models import Score

class ScoreViewSet(viewsets.ModelViewSet):
    queryset = Score.objects.all()
    serializer_class = ScoreSerializer
    authentication_classes = (TokenAuthentication,)

    def retrieve(self, request):
        user = request.user
        queryset = Score.objects.filter(user_id=user.id)
        try:
            score = queryset.get()
            serializer = ScoreSerializer(score)
            return JsonResponse({
                    'status': 'success',
                    'result': serializer.data
                },
                safe=False
            )
        except Score.DoesNotExist:
            return JsonResponse({
                    'status': 'success',
                    'result': {},
                    'message': 'No record found'
                },
                safe=False
            )