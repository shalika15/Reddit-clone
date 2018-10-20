from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Post
from django.utils import timezone

# Create your views here.


@login_required
def create(request):
    if request.method == 'POST':
        if request.POST['title'] and request.POST['url']:
            post = Post()
            post.title = request.POST['title']
            if request.POST['url'].startswith('http://') or request.POST['url'].startswith('https://'):
                 post.url = request.POST['url']
            else:
                post.url = 'http://' + request.POST['url']
            post.pub_date = timezone.datetime.now()
            post.author = request.user
            post.save()
            return redirect('home')
        else:
            return render(request, "Poles/create.html", {'err': "Error:you must include a Title and URL"})

    else:
        return render(request, "Poles/create.html")


def home(request):
    posts = Post.objects.order_by('vote_total')
   # import ipdb; ipdb.set_trace()
    return render(request, 'Poles/home.html', {'p': posts})


def upvote(request, pk1):
    if request.method == 'POST':
        post = Post.objects.get(pk=pk1)
        post.vote_total += 1
        post.save()
        return redirect('home')


def downvote(request, pk2):
    if request.method == 'POST':
        post = Post.objects.get(pk=pk2)
        post.vote_total -= 1
        post.save()
        return redirect('home')
