from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from core import constants
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from datetime import date, datetime
# Create your views here.
