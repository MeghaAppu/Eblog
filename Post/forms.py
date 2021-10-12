from django import forms
from django.forms import widgets
from .models import Post,Genre

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','author_name','genre','content')

        widgets={
            'title': forms.TextInput(attrs={'class':'form-control','width':'13px'}),
            'author_name': forms.Select(attrs={'class':'form-control','style':{'width:20px'}}),
            'genre': forms.Select(attrs={'class':'form-control','style':{'width:20px'}}),
            'content': forms.Textarea(attrs={'class':'form-control','style':{'width:20px'}}),
        }

class UpdatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','content')

        widgets={
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'content': forms.Textarea(attrs={'class':'form-control'}),
        }

