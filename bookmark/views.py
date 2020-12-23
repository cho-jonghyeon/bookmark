from django.shortcuts import render

# Create your views here.
# CRUD가 모든  웹 기능의 중추가 된다.
# views.py에서 모든 CRUD 기능을 준비 한다.
# 뷰는 클래스 형 뷰와 함수 형 뷰로 나눈다.
# 웹 페이지에 접속 한다. => URL을 입력 => 웹 서버가 뷰를 찾아서 동작 => 응답

from  django.views.generic.list import ListView
from  django.views.generic.edit import CreateView, UpdateView, DeleteView
from  django.views.generic.detail import DetailView
from .models import Bookmark
from django.urls import reverse_lazy


class BookmarkListView(ListView):
    model = Bookmark  # 만일 Bookmark에 붉은 색 밑줄이 있으면 동작 안함. 위의 from .models import Bookmark를 해 주어야 함.
    paginate_by = 8   # 페이지 단위 출력 일 경우 한 펜=이지 당 8개로 제한, base.html의 body에서 기본으로 paginate를 정의하고 여기서
                      #  페이지 당 출력 라인을 정의 한다.

class BookmarkCreateView(CreateView):
    model = Bookmark
    fields = ['site_name', 'url']
    success_url = reverse_lazy('List')
    template_name_suffix = '_create'

class BookmarkDetailView(DetailView):
    model = Bookmark
    # fields = ['site_name', 'url']
    # success_url = reverse_lazy('List')
    # template_name_suffix = '_create'

class BookmarkUpdateView(UpdateView):
    model = Bookmark
    fields = ['site_name', 'url']
    # success_url = reverse_lazy('List')
    template_name_suffix = '_update'

class BookmarkDeleteView(DeleteView):
    model = Bookmark
    success_url = reverse_lazy('List')
