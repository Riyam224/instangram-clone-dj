from urllib.parse import urlparse
from django.urls import path
from . import views



app_name = 'insta'


urlpatterns = [
    path('' , views.PostListView.as_view() , name='post_list'),
]
