from django.urls import path, include
from . import views
from django.views import generic

urlpatterns = [
	path('', views.index, name='index'),
	path('<int:blog_id>/', views.detail, name='detail'),
	path('newblog/', views.newblog, name='newblog'),
	path('accounts/', include('django.contrib.auth.urls')),
	path('signup/', views.SignUp, name='SignUp'),
	path('logout/', views.LogOut, name="LogOut")
	]