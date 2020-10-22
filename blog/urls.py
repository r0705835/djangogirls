from blog.views import PostDetailView
from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostListView.as_view(),
         name='post_list'),
    path('post/<int:pk>/', views.PostDetailView.as_view(),
         name='post_detail'),
    path('post/new/', views.PostCreateView.as_view(),
         name='post_new'),
    path('post/<int:pk>/edit/', views.PostEditView.as_view(),
         name='post_edit'),
]
