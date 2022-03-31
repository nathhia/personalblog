from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from core import constants
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from datetime import date, datetime
from django.contrib.auth.forms import UserCreationForm
from rest_framework.decorators import api_view
from django.http import HttpResponse
from project.models import User, Post
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from rest_framework import status
from django.http import JsonResponse
from ..models.user import UserManager
import json

class PostView(ModelViewSet):
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    @action(detail=False, methods=['post'])
    @renderer_classes((TemplateHTMLRenderer, JSONRenderer))
    def savePost(request):
        data = json.loads(request.body)
        data = json.loads(request.body.decode("utf-8"))
        return JsonResponse(data={}, status=status.HTTP_200_OK)