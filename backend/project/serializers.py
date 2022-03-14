from django.contrib.auth.models import User
from rest_framework import serializers
from  models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
         model = User
         fields = ('id', 'first_name', 'last_name', 'username',
                  'password', 'is_active', 'is_superuser', 'email')