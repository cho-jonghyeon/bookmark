from django.urls import path
from .views import *  # "*"은 아래와 같이 여러개의 패스를 모두 포함 할 경우 사용 한다.

 # from .views import BookmarkListView, BookmarkCreateView, BookmarkDetailView


urlpatterns = [
    # http://127.0.0.1/bookmark/????
    # ???/
    path("", BookmarkListView.as_view(), name = 'List'), # 클래스 형 뷰일 경우 반드시 .as_view()를 해 준다. ->함수형 뷰로 변환
    # path의 첫번째를 반드시 공백 없이 ""를 사용 한다.
    path("add/", BookmarkCreateView.as_view(), name = 'add' ),
    path("detail/<int:pk>/", BookmarkDetailView.as_view(), name = 'detail'),
    path("update/<int:pk>/", BookmarkUpdateView.as_view(), name = 'update'),
    path("delete/<int:pk>/", BookmarkDeleteView.as_view(), name = 'delete'),
]