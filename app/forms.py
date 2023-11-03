from django import forms
from .models import Post,Category,Tag

class PostForm(forms.ModelForm):
    categories = forms.ModelMultipleChoiceField(queryset=Category.objects.all())
    tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.all())

    class Meta:
        model = Post
        fields = ('title', 'body', 'categories', 'tags')
