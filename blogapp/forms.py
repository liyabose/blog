from django import forms
from .models import Blog  # or BlogPost if you renamed

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog  # or BlogPost
        fields = ['title', 'author', 'content', 'image']
