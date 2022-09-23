from django.urls import include, path
# from rest_framework import routers
from .routes import CustomReadOnlyRouter
from . import views

router = CustomReadOnlyRouter()
router.register(r'scores', views.ScoreViewSet, basename='scores')

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]