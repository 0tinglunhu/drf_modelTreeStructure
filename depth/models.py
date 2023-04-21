from django.db import models
import uuid

# Create your models here.
class Equipment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=20, null=False)
    brand = models.CharField(max_length=20, null=False)
    model = models.CharField(max_length=20, null=False)


    def __str__(self):
        return self.id

class Component(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=20, null=False)
    brand = models.CharField(max_length=20, null=False)
    model = models.CharField(max_length=20, null=False)
    equipmentId = models.ForeignKey(Equipment, on_delete=models.CASCADE, null=True, related_name="component")

    def __str__(self):
        return self.id

class Sensor(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=10, null=False)
    interval = models.CharField(max_length=10, null=False)
    componentId = models.ForeignKey(Component, on_delete = models.SET_NULL, null=True, related_name="sensor")

    def __str__(self):
        return self.id
