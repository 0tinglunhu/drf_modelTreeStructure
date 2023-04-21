from rest_framework import serializers
from . import models

class SensorList(serializers.ModelSerializer):
    class Meta:
        model = models.Sensor
        fields = '__all__'

class ComponentList(serializers.ModelSerializer):
    sensor = SensorList(many=True)
    class Meta:
        model = models.Component
        fields=(
            'id',
            'name',
            'brand',
            'model',
            'sensor',
        )


class EquipmentSerializer(serializers.ModelSerializer):
    component = ComponentList(many=True)
    class Meta:
        model=models.Equipment

        # fields='__all__'
        fields=(
            'id',
            'name',
            'brand',
            'model',
            'component',
        )
        # depth = 2

class ComponentSerializer(serializers.ModelSerializer):

    class Meta:
        model=models.Component
        fields='__all__'
        depth =1

class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Sensor
        fields='__all__'
        depth =2