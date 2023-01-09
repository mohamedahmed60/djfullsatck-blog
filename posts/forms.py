from django import forms
from .models import Post
from django_summernote.fields import SummernoteTextFormField, SummernoteTextField


class PostForm(forms.Form):
    foo = SummernoteTextFormField()

class FormForSomeModel(forms.ModelForm):
     foo = SummernoteTextField()

# class PostForm(forms.ModelForm):
#     class Meta:
#         model = Post
#         fields = ['title', 'content']

