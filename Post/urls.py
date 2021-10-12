from django.urls import path
from .views import HomeView,PostDetailsView,AddPostView,UpdatePostView,DeletePostView,AddGenreView

urlpatterns = [
    path('', HomeView.as_view(),name="home"),
    path('article/<int:pk>',PostDetailsView.as_view(),name="post_detail"),
    path('create_post/',AddPostView.as_view(),name='create_post'),
    path('add_genre/',AddGenreView.as_view(),name='add_genre'),
    path('article/edit/<str:pk>',UpdatePostView.as_view(),name='update_post'),
    path('article/delete/<int:pk>',DeletePostView.as_view(),name='delete_post'),

]