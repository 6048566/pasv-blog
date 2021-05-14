from django.urls import path
from blog.views import my_test_view, my_first_page, main_feed, get_post

urlpatterns = [
    path('test/', my_test_view),
    path('page/', my_first_page),
    path('list/', main_feed),
    path('post/<int:post_id>/', get_post)
]
