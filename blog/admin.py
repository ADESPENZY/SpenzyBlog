from django.contrib import admin
from .models import Post, Category

# Register your models here.
admin.site.register(Category)

@admin.register(Post)
class PostModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at',)

