# tweets/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from users.models import Tweet

def home(request):
    tweets = Tweet.objects.all().order_by('-created_at')
    return render(request, 'tweets/home.html', {'tweets': tweets})

def create_tweet(request):
    if request.method == 'POST':
        content = request.POST.get('content')
        tweet = Tweet.objects.create(user=request.user, content=content)
        tweet.save()
        return redirect('home')
    return render(request, 'tweets/create_tweets.html')
