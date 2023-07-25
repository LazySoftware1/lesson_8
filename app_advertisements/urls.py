from django.urls import path
from .views import index, top_sellers, advertisement_post, login, register, profile

urlpatterns = [
    path('', index, name='main-page'),
    path('top-sellers', top_sellers, name='top-sellers'),
    path('advertisement-post', advertisement_post, name='advertisement-post'),
    path('login', login, name='login'),
    path('register', register, name='register'),
    path('profile', profile, name='profile')
]