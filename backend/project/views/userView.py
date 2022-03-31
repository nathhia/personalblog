from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny 
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from core import constants
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from datetime import date, datetime
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from rest_framework.decorators import api_view
from django.http import HttpResponse
from project.models import User
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from rest_framework import status
from django.http import JsonResponse
from ..models.user import UserManager
import json


class UserView(ModelViewSet):
    passauthentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (AllowAny,)
    # queryset = User.objects.all()

    # @csrf_exempt
    # @api_view(('POST',))
    # @renderer_classes((TemplateHTMLRenderer, JSONRenderer))
    # def createUser(request):
    # @api_view(('POST',))
    @action(detail=False, methods=['get', 'post'])
    @renderer_classes((TemplateHTMLRenderer, JSONRenderer))
    def createUser(request):
        data = json.loads(request.body)
        data = json.loads(request.body.decode("utf-8"))
        name = data.get('name', None)
        email = data.get('email', None)
        username = data.get('username', None)

        checkUsername = True
        try:
            User.objects.get(username=username)
        except:
            checkUsername = False
        if(checkUsername == True): return JsonResponse(data={"mensage": "username_already_exists"}, status=status.HTTP_401_UNAUTHORIZED, safe=False)

        checkEmail = True
        try:
            User.objects.get(email=email)
        except:
            checkEmail = False
        if(checkEmail == True): return JsonResponse(data={"mensage": "email_already_exists"}, status=status.HTTP_401_UNAUTHORIZED, safe=False)

        sex = data.get('sex', None)
        birthdate = data.get('birthdate', None)
        password = data.get('password', None)
        try:
            moderator = data.get('moderator', False)
        except:
            moderator = False
        birthdateParsed = datetime.strptime(birthdate, "%d/%m/%Y").date()

        newUser = User(username=username, name=name, email=email, is_staff=False, password=password,
                       is_active=True, moderator=moderator, date_joined=date.today(), sex=sex,birthdate=birthdateParsed)
        newUser.set_password(password)
        newUser.save()
        # return Response(status=status.HTTP_200_OK)
        return JsonResponse(data={}, status=status.HTTP_200_OK)