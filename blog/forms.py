from django import forms
from .models import Post, Category, Comment

class PostForm(forms.ModelForm):
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(), 
        empty_label="Select Category",
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Post
        exclude = ('author',)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']  # Only the content of the comment will be filled by the user
        