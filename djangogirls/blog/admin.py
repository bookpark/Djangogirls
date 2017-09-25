from django.contrib import admin
# 애플리케이션 이름이 바뀔수도 있기 때문에 상대경로로 작성하는 것을 추천
from .models import Post


admin.site.register(Post)