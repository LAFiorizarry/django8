from django.contrib.syndication.views import Feed
from myblog.models import Post
from django.urls import reverse

class PostFeed(Feed):
   title = "Posts"
   link = "/latest/feed/"
   description = "Post Feed."

   def items(self):
      return Post.objects.order_by('-published_date')[:5]
		
   def item_title(self, item):
      return item.title
		
   def item_description(self, item):
      return item.text
		
   def item_link(self, item):
      return reverse('blog_detail', args=[item.pk])