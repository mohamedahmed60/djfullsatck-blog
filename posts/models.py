from django.db import models
from django.contrib.auth.models import User # لاستدعا جدول المستخدم وعطاء الصلاحيات

# Create your models here.

class Post(models.Model):
    author = models.ForeignKey(User , on_delete=models.CASCADE , related_name='user_posts')
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=1000)
    image = models.ImageField(upload_to='posts/')

    def __str__(self) -> str: # كيف يمكن ارجاع القيمة لك
        return f"{self.title }-{str(self.author)}"  # لعرض العنون مع المستخدم الذي قام بادخاله

