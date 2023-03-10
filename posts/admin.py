from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post , Category , About
# Register your models here.

class PostModelAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'

admin.site.register(Post,PostModelAdmin)
admin.site.register(Category)
admin.site.register(About, PostModelAdmin)