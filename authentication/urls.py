from django.urls import path

from authentication.views import UserLogin, AuthenticationRootView, UserRegister

urlpatterns = [
    path('',AuthenticationRootView.as_view(), name='authentication-apis'),
    path('login', UserLogin.as_view(), name='login'),
    path('register', UserRegister.as_view(), name='register'),
]
