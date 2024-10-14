from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Post, Account, Comment
from django.contrib.auth.decorators import login_required

@login_required(login_url='login_page')
def dashboard(request):
    profile = request.user.profile
    posts = Post.objects.filter(author=request.user).order_by('-created_at')
    post_count = posts.count()
    total_comments = Comment.objects.filter(post__author=request.user).count()


    context = {
        
        'posts': posts,
        'profile': profile,
        'post_count': post_count,
        'total_comments': total_comments,
    }
    return render(request, 'dashboard/dashboard.html', context)

def post_view(request, username):
    if not request.user.is_authenticated:
        return redirect('login_page')



    user = get_object_or_404(Account, username=username)  # Fetch the user by username from URL
    profile = request.user.profile
    posts = Post.objects.filter(author=user).order_by('-created_at')  # Get all posts by that user
    context = {
        'posts': posts,  # Pass the posts to the template
        'user': user,    # Pass the user to the template
        'profile': profile
    }
    return render(request, 'dashboard/view_post.html', context)