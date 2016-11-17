# -*- coding: utf-8 -*-

from django import forms
from blog.models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ()
        widgets_attrs = {
            'title': forms.TextInput(attrs={
                'class': 'ui container',
                'placeholder': 'Укажите название'
            }),
            'slug': forms.URLInput(attrs={
                'class': 'ui container',
            }),
            'category': forms.Select(attrs={
                'class': 'ui container',
            }),
            'create_at': forms.TextInput(attrs={
                'class': 'ui container',
            }),
            'picture': forms.FileInput(attrs={
                'class': 'ui container',
            }),
            'text': forms.Textarea(attrs={
                'class': 'ui container',
            }),
            'display': forms.CheckboxInput(attrs={
                'class': 'ui container',
            }),
            'like': forms.NumberInput(attrs={
                'class': 'ui container',
            }),
            'dislike': forms.NumberInput(attrs={
                'class': 'ui container',
            }),
        }
