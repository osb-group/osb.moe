from django.conf.urls import url, include
from .views import StoryboardViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'storyboards', StoryboardViewSet)

urlpatterns = [
    url(r'^', include(router.urls))
]