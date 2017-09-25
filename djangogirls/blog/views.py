from django.shortcuts import render

from blog.models import Post


# View에서 인자 이름은 일반적으로 request로 정의한다
def post_list(request):
    # post_list view가 published_date가 존재하는 Post목록만 보여주도록 수정
    posts = Post.objects.filter(published_date__isnull=False)
    context = {
        # posts key의 value는 Queryset
        'posts': posts,
    }
    return render(request, 'blog/post_list.html', context)
