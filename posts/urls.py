from django.urls import path
from .views import all_posts , single_post , new_post , edit_post , delete_post , about

app_name = 'posts'
urlpatterns = [
    path('', all_posts, name='all_posts'),
    path('news', new_post, name='new_post'),

    path('about', about),
    path('<int:id>', single_post, name='single_post'),
    path('<int:id>/edit', edit_post, name='edit_post'),
    path('<int:id>/delete', delete_post, name='delete_post'),
]
