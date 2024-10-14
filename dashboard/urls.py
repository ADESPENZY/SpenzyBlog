from django.urls import path
from . import views 

urlpatterns = [
    path('dashboards/', views.dashboard, name='dashboard-page'),
    path('view_post/<str:username>/', views.post_view, name='view-post-page'),
]