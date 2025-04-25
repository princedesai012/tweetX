from django.shortcuts import render
from .models import tweetX
from .forms import tweetXForm, UserRegistrationForm
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.shortcuts import render
from django.db.models import Q
from .models import tweetX  # Import your tweetX model

def tweet_search(request):
    query = request.GET.get('q')  # Get the search query from the URL
    tweets = tweetX.objects.all()  # Default: Show all tweets

    if query:
        # Filter tweets based on the search query
        tweets = tweetX.objects.filter(
            Q(text__icontains=query) |  # Search in tweet text
            Q(user__username__icontains=query)  # Search in username
        )

    return render(request, 'tweet_search.html', {'tweets': tweets, 'query': query})
# Create your views here.
def index(request):
    return render(request, 'index.html')


def tweetX_list(request):
    tweets = tweetX.objects.all().order_by('-created_at')
    return render(request, 'tweetX_list.html', {'tweets': tweets})

@login_required
def tweet_create(request):
    if request.method == "POST":
        form = tweetXForm(request.POST, request.FILES)
        if form.is_valid(): #provide security
            tweet = form.save(commit=False)#false means not save in database
            tweet.user = request.user
            tweet.save()
            return redirect('tweetX_list')
    else:
        form = tweetXForm()
    return render(request, 'tweetX_form.html', {'form': form})

@login_required
def tweetX_edits(request, tweet_id):
    tweet = get_object_or_404(tweetX, pk = tweet_id, user = request.user)
    if request.method == 'POST':
        form = tweetXForm(request.POST, request.FILES, instance=tweet)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()        
            return redirect('tweetX_list')    
    else:
        form = tweetXForm(instance=tweet)
    return render(request, 'tweetX_form.html', {'form': form})

@login_required
def tweetX_delete(request, tweet_id):
    tweet = get_object_or_404(tweetX, pk = tweet_id, user = request.user)
    if request.method == 'POST':
        tweet.delete()
        return redirect('tweetX_list')
    return render(request, 'tweetX_confirm_delete.html', {'tweet': tweet})


def register(request):
    if request.method =="POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request, user)
            return redirect('tweetX_list')            
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})
        