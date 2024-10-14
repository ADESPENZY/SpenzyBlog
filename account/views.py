from django.shortcuts import render, redirect
from .forms import RegistrationForm , UserProfileForm , ProfileForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib import auth
from .models import Profile
from django.contrib.auth.decorators import login_required


def login_user(request):
    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.info(request, 'You have successfully logged in to your account')
            return redirect('home-page') 
        else:
            messages.error(request, 'Invalid username or password. Please try again.')
            return redirect('login_page')

    # Render the login page
    return render(request, 'account/login.html')

def signup_user(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Automatically create profile and set has_profile to True
            Profile.objects.create(user=user)
            user.has_profile = True
            user.save()
            messages.info(request, 'your account have been created successfully')
            return redirect('login_page')
        else:
            messages.error(request, 'something went wrong')
    else:
        form = RegistrationForm()

    return render (request, 'account/signup.html')

def logout_user(request):
    # Logout the user
    logout(request)
    # Add a success message
    messages.success(request, 'You have logged out of your account successfully.')
    # Redirect to the login page
    return redirect('login_page')

# Profile update view
@login_required
def update_profile(request):
    if request.method == 'POST':
        user_form = UserProfileForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile has been updated!')
            return redirect('dashboard-page')  # Redirect to the profile page after update
    else:
        user_form = UserProfileForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)

    return render(request, 'account/profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })
