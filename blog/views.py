from django.shortcuts import render
from django.http.response import HttpResponse
from blog.models import Post

# Create your views here.

def my_test_view(request):
    return HttpResponse('Some text')

def my_first_page(request):
    return render(request, 'index.html', {
        'my_param': 'My text',
        'my_param2': 'TEXT'
    })


def main_feed(request):
    max_posts_on_page = 10
    page = int(request.GET.get('page', 1))

    start_item = (page-1) * max_posts_on_page
    end_item = start_item + max_posts_on_page

    posts = Post.objects.all()[start_item:end_item]

    return render(request, 'feed.html', {
        'posts_list': posts,
    })


def get_post(request, post_id):
    post = Post.objects.get(id=post_id)

    return render(request, 'page.html', {
        'post': post
    })
