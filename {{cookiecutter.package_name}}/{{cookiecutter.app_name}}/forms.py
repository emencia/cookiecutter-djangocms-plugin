# -*- coding: utf-8 -*-
from django import forms

from djangocms_text_ckeditor.widgets import TextEditorWidget

from {{ cookiecutter.app_name }}.models import {{ cookiecutter.app_name|capitalize }}


class {{ cookiecutter.app_name|capitalize }}PluginForm(forms.ModelForm):
    class Meta:
        model = {{ cookiecutter.app_name|capitalize }}
        widgets = {
            'description': TextEditorWidget,
        }
        fields = [
            'title',
            #'image',
            'description',
        ]
        exclude = []
