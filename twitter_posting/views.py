
from django.shortcuts import render, get_object_or_404, redirect
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import TwitterPosts, Profile
from .forms import TwitterPostForm, UserRegistrationForm

def index(request):

    tweets = TwitterPosts.objects.all()

    context = {
        "tweets": tweets,
    
    }

    return render(request, "twitter_posting/index.html", context)
def users_list(request):

    user_list = User.objects.all()

    context = {
        "user_list": user_list,
    }

    return render(request, "twitter_posting/user_list.html", context)

def user_page(request, id):
    tweeter = get_object_or_404(User, pk=id)
    tweets = tweeter.twitterposts_set.all()

    context = {
        "tweets": tweets,
        "tweeter": tweeter,
    }

    return render(request, "twitter_posting/user_page.html", context)

@login_required
def make_post(request):

    if request.method == "POST":
        form = TwitterPostForm(request.POST)
        if form.is_valid():
            new_message = form.save(commit=False)
            new_message.user_id = request.user.pk
            new_message.save()
            messages.success(request, 'Message Posted!')
            return redirect('twitter_posting:index')
    else:
        form=TwitterPostForm()

    context = {
        "form": form,
    }

    return render(request, "twitter_posting/make_post.html", context)


def register(request):
    if request.method== "POST":
        form = UserRegistrationForm(request.POST)

        if form.is_valid():
            form.save()

            messages.success(request, "User Created!")

            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'],
                                    )
            login(request, new_user)

            return redirect('twitter_posting:user_list')
    else:
        form = UserRegistrationForm()

    context = {
        "form": form,
    }
    return render(request, "twitter_posting/registration.html", context)
# Create your views here.
