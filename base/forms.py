# forms.py
from django import forms
from .models import BlogPost, Comment, Tag

class BlogPostForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = BlogPost
        fields = ['title', 'content', 'tags']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'body']
