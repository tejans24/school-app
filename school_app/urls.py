from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework import viewsets, routers
from accounts.models.user import UserProfile
from accounts.views import accounts_viewsets
from grades.views import grades_viewsets

API_V1_URL = 'api/v1/'

admin.autodiscover()

router = routers.DefaultRouter()

router.register(r'users', accounts_viewsets.UserViewSet)
router.register(r'user_profiles', accounts_viewsets.UserProfileViewSet)
router.register(r'courses', grades_viewsets.CourseViewSet)
router.register(r'assignments', grades_viewsets.AssignmentViewSet)


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'scho ol_app.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^' + API_V1_URL, include(router.urls)),
    url(r'^' + API_V1_URL + 'oauth2/', include('provider.oauth2.urls', namespace='oauth2')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)
