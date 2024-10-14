from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Post, Comment
from .forms import PostForm, CommentForm
from django.contrib.auth.decorators import login_required


# View for home page displaying categories
def home(request):
    categories = Category.objects.all()
    posts = Post.objects.all()

    # Retrieve the latest two posts in each category
    technology_posts = Post.objects.filter(category__name='Technology').order_by('-created_at')[:2]
    politics_posts = Post.objects.filter(category__name='Politics').order_by('-created_at')[:2]
    sport_posts = Post.objects.filter(category__name='Sport').order_by('-created_at')[:2]
    business_posts = Post.objects.filter(category__name='Business').order_by('-created_at')[:2]
    lifestyle_posts = Post.objects.filter(category__name='Lifestyle').order_by('-created_at')[:2]
    health_posts = Post.objects.filter(category__name='Health').order_by('-created_at')[:2]
    entertainment_posts = Post.objects.filter(category__name='Entertainment').order_by('-created_at')[:2]

    # Split them into latest and second-to-last
    latest_technology_post = technology_posts[0] if technology_posts else None
    second_technology_post = technology_posts[1] if len(technology_posts) > 1 else None
    
    latest_politics_post = politics_posts[0] if politics_posts else None
    second_politics_post = politics_posts[1] if len(politics_posts) > 1 else None

    latest_sport_post = sport_posts[0] if sport_posts else None
    second_sport_post = sport_posts[1] if len(sport_posts) > 1 else None

    latest_business_post = business_posts[0] if business_posts else None
    second_business_post = business_posts[1] if len(business_posts) > 1 else None

    latest_lifestyle_post = lifestyle_posts[0] if lifestyle_posts else None
    second_lifestyle_post = lifestyle_posts[1] if len(lifestyle_posts) > 1 else None

    latest_health_post = health_posts[0] if health_posts else None
    second_health_post = health_posts[1] if len(health_posts) > 1 else None

    latest_entertainment_post = entertainment_posts[0] if entertainment_posts else None
    second_entertainment_post = entertainment_posts[1] if len(entertainment_posts) > 1 else None

    return render(request, 'blog/home.html', {
        'categories': categories,
        'posts': posts,
        'latest_technology_post': latest_technology_post,
        'second_technology_post': second_technology_post,
        'latest_politics_post': latest_politics_post,
        'second_politics_post': second_politics_post,
        'latest_sport_post': latest_sport_post,
        'second_sport_post': second_sport_post,
        'latest_business_post': latest_business_post,
        'second_business_post': second_business_post,
        'latest_lifestyle_post': latest_lifestyle_post,
        'second_lifestyle_post': second_lifestyle_post,
        'latest_health_post': latest_health_post,
        'second_health_post': second_health_post,
        'latest_entertainment_post': latest_entertainment_post,
        'second_entertainment_post': second_entertainment_post,
    })


# View for displaying posts in a specific category
def category_posts(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts = Post.objects.filter(category=category)
    return render(request, 'blog/category_posts.html', {'category': category, 'posts': posts})

@login_required(login_url='login_page')
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('home-page')  # Redirect to home page after successful post creation
    else:
        form = PostForm()
    return render(request, 'blog/create_post.html', {'form': form})

@login_required(login_url='login_page')
def edit_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/edit_post.html', {'form': form})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.all()

    if request.method == 'POST':
        if request.user.is_authenticated:
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.post = post
                comment.author = request.user
                comment.save()
                return redirect('post_detail', post.pk)
        else:
            return redirect('login_page')  # Make sure the name matches the URL pattern
    else:
        form = CommentForm()

    context = {
        'post': post,
        'comments': comments,
        'form': form,
    }

    return render(request, 'blog/post_detail.html', context)


@login_required(login_url='login_page')
def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('home-page')
    return render(request, 'blog/confirm_delete.html', {'post': post})

def contact(request):
    return render(request, 'blog/contact.html')

def about(request):
    return render(request, 'blog/about.html')












# def home(request):
#     categories = Category.objects.all()
#     posts = Post.objects.all()
    
#     # Get the latest post in the named category
#     latest_technology_post = Post.objects.filter(category__name='Technology').order_by('-created_at').first()
#     latest_politics_post = Post.objects.filter(category__name='Politics').order_by('-created_at').first()
#     latest_sport_post = Post.objects.filter(category__name='Sport').order_by('-created_at').first()
#     latest_business_post = Post.objects.filter(category__name='Business').order_by('-created_at').first()
#     latest_lifestyle_post = Post.objects.filter(category__name='Lifestyle').order_by('-created_at').first()
#     latest_health_post = Post.objects.filter(category__name='Health').order_by('-created_at').first()
#     latest_entertainment_post = Post.objects.filter(category__name='Entertainment').order_by('-created_at').first()

#     return render(request, 'blog/home.html', {
#         'categories': categories,
#         'posts': posts,
#         'latest_technology_post': latest_technology_post,  # Pass the latest post to the template
#         'latest_politics_post': latest_politics_post,
#         'latest_sport_post': latest_sport_post,
#         'latest_business_post': latest_business_post,
#         'latest_lifestyle_post': latest_lifestyle_post,
#         'latest_health_post': latest_health_post,
#         'latest_entertainment_post': latest_entertainment_post,
#     })