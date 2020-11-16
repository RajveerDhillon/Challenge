from django.shortcuts import render
from users.models import Profile

def home(request):
    context = {
        'posts': Profile.objects.all()
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
