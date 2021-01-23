from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup_view, name="signup"),
    path('signup_temp/', views.signup_view_temp, name="signup_temp"),
    path('login/', views.login_view, name="login"),
    path('login_new/', views.login_view_new, name="login_new"),
    path('login_1/', views.login_view_1, name="login1"),
    path('logout/', views.logout_view, name="logout"),
]
