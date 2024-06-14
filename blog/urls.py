from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('search/<str:q>/', views.PostSearch.as_view()),
    path('delete_comment/<int:pk>/', views.delete_comment),
    path('update_comment/<int:pk>/', views.CommentUpdate.as_view()),
    path('update_post/<int:pk>/', views.PostUpdate.as_view()),
    path('create_post/', views.PostCreate.as_view()),
    path('tag/<str:slug>/', views.tag_page),
    path('category/<str:slug>/', views.category_page),
    path('<int:pk>/new_comment/', views.new_comment),
    path('', views.PostList.as_view()),
    path('<int:pk>/', views.PostDetail.as_view()),
    path('sign-in/', auth_views.LoginView.as_view(template_name='blog/signin.html')),
    path('sign-out/', views.sign_out_view),
]