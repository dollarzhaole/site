__author__ = 'dollar'

from tinymce.widgets import TinyMCE
from django import forms

class BlogForm(forms.Form):
    caption = forms.CharField(label='title', max_length=100)
    content = forms.CharField(widget=forms.Textarea)
    # content = forms.CharField(widget=TinyMCE(attrs={'cols': 60, 'rows': 20}))

class TagForm(forms.Form):
    tag_name = forms.CharField()
