from django.db import models
from agents.models import Agent
from django.utils import timezone

class Inquiry(models.Model):
    name = models.CharField(max_length=200)
    property_name = models.CharField(max_length=200)
    email =models.CharField(max_length=200)
    phone =models.CharField(max_length=200)
    message = models.TextField(max_length=500)
    date_inquiry=models.DateTimeField(default=timezone.now, blank=True)
    agent=models.ForeignKey(Agent, null=True, on_delete=models.SET_NULL)
    def __str__(self):
        return self.name