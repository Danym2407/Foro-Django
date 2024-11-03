from django.urls import path
from . import views
from user import views as user_views
from .views import (PostListView, 
                    PostDetailView, 
                    PostCreateView,
                    PostUpdateView,
                    PostDeleteView
                )


urlpatterns = [
    path('', PostListView.as_view(), name= 'blog-home'),
    path('post/<int:pk>', PostDetailView.as_view(), name= 'post-detail'), #para ver cada post de manera individual
    path('post/new', PostCreateView.as_view(), name= 'post-create'), #para ver cada post de manera individual
    path('post/<int:pk>/update', PostUpdateView.as_view(), name= 'post-update'), #para actualizar cada post
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name= 'post-delete'), #para actualizar cada post
    path('register/', user_views.register, name='register'),
    path('about/', views.about, name= 'blog-about'),
]

