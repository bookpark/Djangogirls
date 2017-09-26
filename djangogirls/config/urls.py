"""djangogirls URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from blog.views import post_list, post_detail

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', post_list, name='post_list'),
    # psot/<숫자 1개 이상/ 이 가능하도록 정규표현식 작성
    # 해당 숫자는 그룹으로 감싸고 'pk'라는 그룹명을 지정
    url(r'^post/detail/(?P<pk>\d+)/', post_detail, name='post_detail'),
]
