from django.urls import path
from . import views

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("chat/", views.ChatView.as_view(), name="chat"),
    path("history/", views.SearchHistoryView.as_view(), name="search_history"),
    # 로그인/로그아웃 URL 등 추가
]
