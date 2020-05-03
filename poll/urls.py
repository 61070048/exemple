from django.contrib import admin
from django.conf.urls import url, include
from rest_framework import routers
from .views import QuestionViewSet, ChoiceViewSet

router = routers.DefaultRouter()
router.register(r'choices', ChoiceViewSet)
router.register(r'questions', QuestionViewSet)

urlpatterns = [
    url(r'^api/', include(router.urls)),
    url(r'^api/', include('rest_framework.urls', namespace='rest_framework'))
]
