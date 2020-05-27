from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from core.models import Tweet, Hashtag

import re

# GET / -> display html
# POST / -> create new note and redirect to GET /


# Create your views here.
def splash(request):
    if not request.user.is_authenticated:
        return redirect('/home')

    if request.method == "POST":
        body = request.POST["body"]
        hashtags = set(re.findall(r"#(\w+)", body))
        t = Tweet.objects.create(body=body, author=request.user)
        for h in hashtags:
            hashtag, created = Hashtag.objects.get_or_create(name=h)
            hashtag.tweet.add(t)
        return redirect("/")

    tweets = Tweet.objects.all().order_by('-time')
    tlist = []
    for t in tweets:
        if request.user in t.liked_by.all():
            liked = True
        else:
            liked = False
        tlist.append({"tweet": t, "liked": liked})
    hashtag_list = Hashtag.objects.all()
    return render(request, "splash.html", {"tweets": tlist, "hashtags": hashtag_list})


def accounts(request):
    return render(request, "accounts.html", {})


def hashtag(request):
    h = Hashtag.objects.get(name=request.GET['name'])
    tweets = h.tweet.all()
    tlist = []
    for t in tweets:
        if request.user in t.liked_by.all():
            liked = True
        else:
            liked = False
        tlist.append({"tweet": t, "liked": liked})
    return render(request, "hashtag.html", {"hashtag": h, "tweets": tlist})


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
    return render(request, 'accounts.html', {})


def signup_view(request):
    if request.method == "POST":
        user = User.objects.create_user(username=request.POST['username'], password=request.POST['password'])
        login(request, user)
        return redirect('/')
    return render(request, 'accounts.html', {})


def logout_view(request):
    logout(request)
    return redirect("/home")


def delete(request):
    t = Tweet.objects.get(id=request.GET['id'])
    for h in Hashtag.objects.filter(tweet=t):
        if len(h.tweet.all()) == 1:
            h.delete()
    t.delete()
    return redirect('/')


def like(request):
    t = Tweet.objects.get(id=request.GET['id'])
    t.likes += 1
    t.save()
    t.liked_by.add(request.user)
    return redirect('/')


def unlike(request):
    t = Tweet.objects.get(id=request.GET['id'])
    t.likes -= 1
    t.save()
    t.liked_by.remove(request.user)
    return redirect('/')


def profile(request):
    user = User.objects.get(username=request.GET['user'])
    tweets = Tweet.objects.filter(author=user).order_by('-time')
    tlist = []
    for t in tweets:
        if request.user in t.liked_by.all():
            liked = True
        else:
            liked = False
        tlist.append({"tweet": t, "liked": liked})
    return render(request, "profile.html", {"author": user, "tweets": tlist})


def view_like(request):
    t = Tweet.objects.all().get(id=request.GET['id'])
    ulist = t.liked_by.all()
    return render(request, "view_like.html", {"tweet": t, "liked_by": ulist})


def home(request):
    return render(request, "home.html")
