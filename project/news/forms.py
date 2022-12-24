from django import forms
from django.core.exceptions import ValidationError
from .models import *



class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'text',
            'image',
            'video',
            'docx',
            'category'
            ]

class ResponseForm(forms.ModelForm):
    class Meta:
        model = Response
        fields = [
            'text',
        ]

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = [
            'bio',
            'avatar',
        ]
