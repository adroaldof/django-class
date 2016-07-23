from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^create/$', views.create_post, name='create'),
    url(r'^list/$', views.list_posts, name='list'),
    url(r'^update/(?P<post_id>[0-9]+)/$', views.update_post, name='update'),
    url(r'^view/(?P<post_id>[0-9]+)/$', views.view_post, name='view'),
    url(r'^delete/(?P<post_id>[0-9]+)/$', views.delete_post, name='delete'),
]
