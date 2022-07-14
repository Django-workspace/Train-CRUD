from django import forms
from .models import *

class T_Forms(forms.ModelForm):
    class Meta:
        model = Trainee_model
        fields = "__all__"