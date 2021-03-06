from django.contrib.auth import get_user_model
from django.http import HttpResponse
from django.shortcuts import render, redirect

from blog.models import Post

User = get_user_model()


# View에서 인자 이름은 일반적으로 request로 정의한다
def post_list(request):
    # post_list view가 published_date가 존재하는 Post목록만 보여주도록 수정
    posts = Post.objects.filter(published_date__isnull=False)
    context = {
        # posts key의 value는 Queryset
        'posts': posts,
    }
    return render(request, 'blog/post_list.html', context)


def post_created(request):
    posts = Post.objects.filter(published_date__isnull=True)
    context = {
        'posts': posts,
    }
    return render(request, 'blog/post_created.html', context)


# post_detail 기능을 하는 함수를 구현
# 'post'라는 key로 Post.objects.first()에 해당하는 Post 객체를 전달
# 템플릿은 'blog/post_detail.html'을 사용
def post_detail(request, pk):
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return HttpResponse('페이지를 찾을 수 없습니다.', status=404)
    context = {
        'post': post,
    }
    return render(request, 'blog/post_detail.html', context)


def post_add(request):
    if request.method == 'POST':
        # request.POST에서 'title', 'content' 키에 해당하는 value를 받아오기
        # 새 Post 객체를 생성 (save() 호출없음 단순 인스턴스 생성)
        # 생성한 후에는 해당 객체의 title, content를 HttpResponse로 전달

        # title이나 content 값이 오지 않았을 경우에는 객체를 생성하지 않고 다시 작성페이지로 이동
        #   extra) 작성페이지로 이동 시 '값을 입력해주세요'라는 텍스트를 어딘가에 표
        title = request.POST.get('title')
        content = request.POST.get('content')
        author = User.objects.get(username='admin')

        if title and content:
            post = Post.objects.create(
                author=author,
                title=title,
                content=content
            )
            checkbox = request.POST.get('check-checkbox')
            if checkbox:
                post.publish()
            return redirect('post_detail', pk=post.pk)

        context = {
            'title': title,
            'content': content,
        }
    else:
        context = {}

    return render(request, 'blog/post_form.html', context)


def post_delete(request, pk):
    if request.method == 'POST':
        post = Post.objects.get(pk=pk)
        post.delete()
        return redirect('post_list')
    return HttpResponse('Permission Denied', status=403)


def post_publish(request, pk):
    if request.method == 'POST':
        post = Post.objects.get(pk=pk)
        post.publish()
        return redirect('post_created')
    return HttpResponse('Permission Denied', status=403)