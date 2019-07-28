from django.urls import path
from .views import list_view, detail_view, add_model
from myblog.feeds import LatestEntriesFeed

urlpatterns = [
    path('', list_view, name="blog_index"),
    path('posts/<int:post_id>/', detail_view, name="blog_detail"),
    path('post/new/', add_model, name='post_new'),
    path('post/feed/', LatestEntriesFeed())
]