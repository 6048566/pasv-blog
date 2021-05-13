from django.urls import path
from blog.views import my_test_view, my_first_page

urlpatterns = [
    path('test/', my_test_view),
    path('page/', my_first_page)
]
