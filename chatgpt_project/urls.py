from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("admin/", admin.site.urls),  # Django 관리자 페이지
    path("", include("chat.urls")),  # chat 앱의 URL 연결
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="chat/login.html"),
        name="login",
    ),  # 로그인 페이지
    path(
        "logout/", auth_views.LogoutView.as_view(next_page="/login/"), name="logout"
    ),  # 로그아웃 후 리디렉션
]
