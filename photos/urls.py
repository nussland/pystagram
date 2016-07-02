from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from .views import *

app_name = 'photos'

urlpatterns = [
    url(r'^delete/(?P<pk>[0-9]+)/$', login_required(PhotoDelete), name='delete_photo'),
    url(r'^view/(?P<pk>[0-9]+)/$', login_required(PhotoView.as_view()), name='view_photo'),
    url(r'^create/$', login_required(PhotoCreate.as_view()), name='create_photo'),
    url(r'^$', PhotoList.as_view(), name='list_photos'),
]

