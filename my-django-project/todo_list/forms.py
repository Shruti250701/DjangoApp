from django import forms
from .models import TaskList

class PostForm(forms.ModelForm):

    class Meta:
        model = TaskList
        fields = '__all__'

class UpdateForm(forms.ModelForm):

    class Meta:
        model = TaskList
        fields = '__all__'