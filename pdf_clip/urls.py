from django.urls import path, include
from . import views

from rest_framework import routers
router = routers.DefaultRouter()
router.register(r'clips', views.ClipViewSet, 'clipView')
router.register(r'files', views.FileViewSet, 'fileView')

urlpatterns = [
    path("clip", views.clip, name="clip"),
    path("review", views.review, name="review"),
    path("build", views.build, name="build"),
    path("test", views.test, name="test"),
    path("", views.upload, name="upload"),

    path("api/files", views.FileViewSet2.as_view(), name='fileView'),
    path("api/clips", views.ClipViewSet2.as_view(), name='clipView'),
    
    path("api", include(router.urls)),
    path("api-auth", include('rest_framework.urls', namespace='rest_framework')),
]