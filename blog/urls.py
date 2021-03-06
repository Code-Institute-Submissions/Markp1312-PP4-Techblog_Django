from django.urls import path
from .views import (
    HomePage, ArticleDetailView, 
    AddPostView, EditPostView, 
    DeletePost, AddCategoryView, 
    CategoryView, CategoryListView, 
    LikeView, AddCommentView
)

urlpatterns = [
    path('', HomePage.as_view(), name="home"),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article-detail'),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('add_category/', AddCategoryView.as_view(), name='add_category'),
    path('article/edit/<int:pk>', EditPostView.as_view(), name='edit_post'),
    path('article/<int:pk>/remove', DeletePost.as_view(), name='delete_post'),
    path('category/<str:cats>/', CategoryView, name='category'),
    path('category-list/', CategoryListView, name='category-list'),
    path('like/<int:pk>', LikeView, name='like_post'),
    path('article/<int:pk>/comment/', AddCommentView.as_view(), name='add_comment'),
]
