from django.forms import ModelForm, forms
from .models import Post


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ["title", "description", "author", "image"]

