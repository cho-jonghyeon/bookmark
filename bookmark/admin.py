from django.contrib import admin
from .models import Bookmark
# 내가 만든 모델을 관리자 페이지에서 관리 할 수 있도록 등록
# Register your models here.

admin.site.register(Bookmark)
