from django.forms import ModelForm
from django import forms
from .models import Post


class PostForm(ModelForm):
        class Meta:
            model = Post
            fields = ['group', 'text']


        def clean_text(self):
            data = self.cleaned_data["text"]
            if len(self.cleaned_data.get('text')) == 0:
                raise forms.ValidationError("Напишите текст")
            return data
        