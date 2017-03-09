from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index_login, name='index_login'),
    url(r'^list_users$', views.list_users, name='list_users'),
    url(r'^add_user/$', views.add_user, name='add_user'),
    url(r'^delete_user/(?P<user_id>[0-9]+)$', views.delete_user, name='delete_user'),
]
