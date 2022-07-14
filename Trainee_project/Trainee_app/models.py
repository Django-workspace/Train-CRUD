from inspect import stack
from django.db import models
import uuid

class Trainee_model(models.Model):
    id=models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, serialize=True)
    names=models.CharField(max_length=100)
    dob=models.DateField()
    stack=models.CharField(max_length=50)
    createdOn=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.names} to {self.createdOn} "