from django.urls import path
from .views import home, blogpost_create, blogpost_update, blogpost_delete
from django.urls import path
from django.contrib.auth import views as auth_views
from main import views

urlpatterns = [
    path('home', home, name='home'),
    path('create/', blogpost_create, name='blogpost_create'),
    path('update/<int:pk>/', blogpost_update, name='blogpost_update'),
    path('delete/<int:pk>/', blogpost_delete, name='blogpost_delete'),
    path('', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    # path('blogpost/<int:pk>/', views.blogpost_detail, name='blogpost_detail'),
    path('blogpost/<int:blogpost_id>/', views.blogpost_detail, name='blogpost_detail'),
    
    path('category', views.category_list, name='category_list'),
    path('category/<int:pk>/', views.category_detail, name='category_detail'),
    path('category/create/', views.category_create, name='category_create'),
    path('category/<int:pk>/update/', views.category_update, name='category_update'),
    path('category/<int:pk>/delete/', views.category_delete, name='category_delete'),

]
