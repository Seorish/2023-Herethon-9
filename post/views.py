from django.shortcuts import render, redirect
from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


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
    page = request.GET.get('page')

    # 한 페이지에 게시글 2개를 보여줌
    paginator = Paginator(posts, 2)

    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger: # 첫번째 페이지 접속시 나는 오류 해결
        page = 1
        page_obj = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        page_obj = paginator.page(page)

    leftIndex = (int(page) - 2)
    if leftIndex < 1:
        leftIndex = 1

    rightIndex = (int(page) + 2)

    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages

    custom_range = range(leftIndex, rightIndex+1)

    context = {
        'posts': posts,
        'custom_range': custom_range,
        'page_obj': page_obj,
        'paginator': paginator,
    }

    return render(request, 'html/post_list.html', context)


def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    context = {
        'post': post,
    }

    return render(request, 'html/post_detail.html', context)

