from django.conf.urls import patterns, include, url
from rest_framework import viewsets, routers
from django.contrib import admin
from grades.views import grades_viewsets
from accounts.views import accounts_viewsets


API_V1_URL = 'api/v1/'


router = routers.DefaultRouter()
router.register(r'course', grades_viewsets.CourseViewSet)
router.register(r'assignment', grades_viewsets.AssignmentViewSet)
router.register(r'score', grades_viewsets.ScoreViewSet)
router.register(r'user', accounts_viewsets.UserViewSet)
router.register(r'student', accounts_viewsets.StudentViewSet)
router.register(r'teacher', accounts_viewsets.TeacherViewSet)

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'scho ol_app.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^' + API_V1_URL, include(router.urls)),

    url(r'^' + API_V1_URL + 'oauth2/', include('provider.oauth2.urls', namespace='oauth2')),
    url(r'^api/api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)
