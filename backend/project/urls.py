from rest_framework import viewsets, routers
from django.urls import path, include
from .views.userView import UserView
from .views.userControlView import UserControlView

router = routers.DefaultRouter()

urlpatterns = [
    path('users/register/', UserView.createUser),
    path('users/logout/', UserControlView.logout),
    path('', include(router.urls)),
]