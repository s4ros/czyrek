from django.conf.urls import url

from . import views

urlpatterns = [
    # general
    url(r'^$', views.index_login, name='index_login'),
    url(r'^logout/$', views.logout_user, name='logout'),
    url(r'^index/$', views.index_after_login, name='index_after_login'),
    # users
    url(r'^list_users/$', views.list_users, name='list_users'),
    url(r'^add_user/$', views.add_user, name='add_user'),
    url(r'^delete_user/(?P<user_id>[0-9]+)$', views.delete_user, name='delete_user'),
    # candidates
    url(r'^list_candidates/$', views.list_candidates, name='list_candidates'),
    url(r'^add_candidate/$', views.add_candidate, name='add_candidate'),
    url(r'^delete_candidate/(?P<candidate_id>[0-9]+)$', views.delete_candidate, name='delete_candidate'),
    # schools
    url(r'^list_schools/$', views.list_schools, name='list_schools'),
    # languages
    url(r'^list_languages/$', views.list_languages, name='list_languages'),
    # profiles
    url(r'^list_profiles/$', views.list_profiles, name='list_profiles'),
    # subjects
    url(r'^list_subjects/$', views.list_subjects, name='list_subjects'),
]
