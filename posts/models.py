from django.db import models
from django.contrib.auth.models import User # لاستدعا جدول المستخدم وعطاء الصلاحيات
from django.utils import timezone
# Create your models here.

class Post(models.Model):
    author = models.ForeignKey(User , on_delete=models.CASCADE , related_name='user_posts')
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=10000000)
    image = models.ImageField(upload_to='posts/')
    publish_data = models.DateField(default=timezone.now)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='post_category')

    def __str__(self) -> str: # كيف يمكن ارجاع القيمة لك
        return f"{self.title }-{str(self.author)}"  # لعرض العنون مع المستخدم الذي قام بادخاله

# علاقة  category و  post العلاقة بين ال
# one to many
class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.name.__str__()

class About(models.Model):
    blog_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='about')
    subtitle = models.TextField(max_length=100000000)
    aboutme = models.TextField(max_length=100000000)
    tw_link = models.URLField()
    tk_in_link = models.URLField()
    github_link = models.URLField()