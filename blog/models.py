from django.db import models
from django.core.validators import FileExtensionValidator
from account.models import Account
from django.utils.text import slugify

class Category(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(unique=True, blank=True)  # Allow blank for automatic slug generation

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:  # Only set the slug if it's not already set
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
class Post(models.Model):
    author = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='post-images', validators=[FileExtensionValidator(['png', 'jpg', 'webp'])])
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='posts')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    def comments(self):
        return self.comments.all()  # Use 'comments' due to related_name

    def comment_count(self):
        return self.comments.all().count()  # Use 'comments' due to related_name
    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')  # Link to the Post model
    author = models.ForeignKey(Account, on_delete=models.CASCADE)  # Link to the Account model for the user
    content = models.TextField()  # Comment content
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set the timestamp when the comment is created
    updated_at = models.DateTimeField(auto_now=True)  # Automatically update the timestamp when the comment is updated

    def __str__(self):
        return f'Comment by {self.author} on {self.post}'

