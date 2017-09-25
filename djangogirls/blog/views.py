from django.shortcuts import render

from blog.models import Post


# View에서 인자 이름은 일반적으로 request로 정의한다
def post_list(request):
    posts = Post.objects.all()
    context = {
        # posts key의 value는 Queryset
        'posts': posts,
    }
    return render(request, 'blog/post_list.html', context)
