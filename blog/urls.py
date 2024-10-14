from  django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home-page'),
    path('category/<slug:slug>/', views.category_posts, name='category_posts'),
    path('create-post/', views.create_post, name='create_post'),
    path('edit-post/<int:pk>', views.edit_post, name='edit_post'),
    path('post-detail/<int:pk>', views.post_detail, name='post_detail'),
    path('delete-post/<int:pk>', views.delete_post, name='delete_post'),
    path('contact/', views.contact, name='contact-page'),
    path('about/', views.about, name='about-page'),
]