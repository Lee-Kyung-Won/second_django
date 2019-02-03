from django.urls import path, re_path
from django.contrib.auth import views as auth_views
from django.conf import settings
from . import views


urlpatterns = [
    path('signup/', views.signup, name='signup'),
    re_path(r'^login/$', auth_views.login, name='login',
         kwargs={'template_name': 'accounts/login_form.html'}),
    re_path(r'^logout/$', auth_views.logout, name='logout',
         kwargs={'next_page': settings.LOGIN_URL}),
    path('profile/', views.profile, name='profile'),
]