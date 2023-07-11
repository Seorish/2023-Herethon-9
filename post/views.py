from django.shortcuts import render, redirect
from django.shortcuts import render, redirect, get_object_or_404
from .models import Post


def create(request):
    if request.method == 'POST':
        post = Post()
        post.title = request.POST['title']
        post.body = request.POST['body']
        post.category = request.POST['category']
        post.save()
        return redirect("create")

    return render(request, "html/post.html")


def post_list(request):
    # 모든 게시글 가져오기
    posts = Post.objects.all()

    context = {
        'posts': posts,
    }

    return render(request, 'html/post_list.html', context)

def post_detail(request, post_id):
    # 게시글 가져오기
    post = get_object_or_404(Post, pk=post_id)

    context = {
        'post': post,
    }

    return render(request, 'html/post_detail.html', context)