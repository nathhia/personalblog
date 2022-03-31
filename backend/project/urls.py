from rest_framework import viewsets, routers
from django.urls import path, include
from .views.userView import UserView
from .views.userControlView import UserControlView
from .views.postView import PostView

router = routers.DefaultRouter()

urlpatterns = [
    path('users/register/', UserView.createUser),
    path('users/logout/', UserControlView.logout),
    path('post/save/', PostView.savePost),
    path('', include(router.urls)),
]