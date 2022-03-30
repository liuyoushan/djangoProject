from django.urls import path
from . import views

app_name = 'zlauth'
urlpatterns = [
    path('login',views.LoginView.as_view(),name='login'),
    path('user',views.UserView.as_view(),name='user'),
    path('avatar',views.AvatarUploadView.as_view(),name='avatar'),

    # 登录页面
    path('loginhtml', views.login_html.login_html, name='login_html'),

]