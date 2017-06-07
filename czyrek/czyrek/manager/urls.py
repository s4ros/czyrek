from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    # general
    url(r'^$', views.index_login, name='index_login'),
    url(r'^logout$', views.logout_user, name='logout'),
    url(r'^index$', views.index_after_login, name='index_after_login'),
    # users
    url(r'^list_users$', views.list_users, name='list_users'),
    url(r'^add_user$', views.add_user, name='add_user'),
    url(r'^delete_user/(?P<user_id>[0-9]+)$', views.delete_user, name='delete_user'),
    url(r'^edit_user/(?P<user_id>[0-9]+)$', views.edit_user, name='edit_user'),
    # candidates
    url(r'^list_candidates$', views.list_candidates, name='list_candidates'),
    url(r'^add_candidate$', views.add_candidate, name='add_candidate'),
    url(r'^delete_candidate/(?P<candidate_id>[0-9]+)$', views.delete_candidate, name='delete_candidate'),
    url(r'^edit_candidate/(?P<candidate_id>[0-9]+)$', views.edit_candidate, name='edit_candidate'),
    # edit active_school
    url(r'^edit_active_school/(?P<candidate_id>[0-9]+)/(?P<active_school>[0-9]+)$', views.edit_active_school, name='edit_active_school'),
    url(r'^edit_active_school$', views.edit_active_school, name='edit_active_school'),
    # schools
    url(r'^list_schools$', views.list_schools, name='list_schools'),
    url(r'^add_school$', views.add_school, name='add_school'),
    url(r'^delete_school/(?P<school_id>[0-9]+)$', views.delete_school, name='delete_school'),
    url(r'^edit_school/(?P<school_id>[0-9]+)$', views.edit_school, name='edit_school'),
    # languages
    url(r'^list_languages$', views.list_languages, name='list_languages'),
    url(r'^add_language$', views.add_language, name='add_language'),
    url(r'^delete_language/(?P<language_id>[0-9]+)$', views.delete_language, name='delete_language'),
    url(r'^edit_language/(?P<language_id>[0-9]+)$', views.edit_language, name='edit_language'),
    # profiles
    url(r'^list_profiles$', views.list_profiles, name='list_profiles'),
    url(r'^add_profile$', views.add_profile, name='add_profile'),
    url(r'^delete_profile/(?P<profile_id>[0-9]+)$', views.delete_profile, name='delete_profile'),
    url(r'^edit_profile/(?P<profile_id>[0-9]+)$', views.edit_profile, name='edit_profile'),
    # subjects
    url(r'^list_subjects$', views.list_subjects, name='list_subjects'),
    url(r'^add_subject$', views.add_subject, name='add_subject'),
    url(r'^delete_subject/(?P<subject_id>[0-9]+)$', views.delete_subject, name='delete_subject'),
    url(r'^edit_subject/(?P<subject_id>[0-9]+)$', views.edit_subject, name='edit_subject'),
    # simulation
    url(r'^simulation$', views.simulation, name='simulation'),
    url(r'^simulation/(?P<candidate_id>[0-9]+)/(?P<active_school>[0-9]+)$', views.simulation, name='simulation'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
