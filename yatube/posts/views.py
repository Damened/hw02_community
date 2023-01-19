from django.shortcuts import render
from .models import Post, Group
from django.shortcuts import render, get_object_or_404


number_post = 10


def index(request):
    posts = Post.objects.order_by('-pub_date')[:number_post]
    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context)
