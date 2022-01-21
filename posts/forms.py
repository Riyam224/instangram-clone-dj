import imp
from django import forms 
from .models import Post



class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title' , 'caption' , 'profile', 'image')
        widgets = {
            'title': forms.TextInput(attrs={
                'class':'form-control' ,
                'placeholder': 'title of the  new post'
            }) ,
            'caption' : forms.Textarea(attrs={
                'class':'form-control' ,
                'placeholder': 'caption of the new post'
            })
        }

