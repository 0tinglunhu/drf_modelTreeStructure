from django.shortcuts import render
from rest_framework import viewsets, generics, status, filters
from rest_framework.response import Response
import django_filters
from django_filters.rest_framework import DjangoFilterBackend, FilterSet
from django.db.models import Q, F, Count, Avg, Sum, Max, Min
from json import dumps
from enum import Enum
import json, os
import requests
from django.http import HttpResponse
from ctypes import *

from . import models
from . import serializers
# Create your views here.
class EquipmentViewSet(viewsets.ModelViewSet):
    queryset = models.Equipment.objects.all()
    # queryset = models.Equipment.objects.filter(Q(component__isnull = False))
    serializer_class = serializers.EquipmentSerializer
    filter_backends = [DjangoFilterBackend]

class ComponentViewSet(viewsets.ModelViewSet):
    queryset = models.Component.objects.all()
    serializer_class = serializers.ComponentSerializer
    filter_backends = [DjangoFilterBackend]

class SensorViewSet(viewsets.ModelViewSet):
    queryset = models.Sensor.objects.all()
    serializer_class = serializers.SensorSerializer
    filter_backends = [DjangoFilterBackend]



