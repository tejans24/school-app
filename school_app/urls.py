from django.conf.urls import patterns, include, url
from rest_framework import viewsets, routers
from django.contrib import admin
from grades.models import Course, Score, Assignment

API_V1_URL = 'api/v1/'


class CourseViewSet(viewsets.ModelViewSet):
    model = Course


class AssignmentViewSet(viewsets.ModelViewSet):
    model = Assignment


class ScoreViewSet(viewsets.ModelViewSet):
    model = Score

admin.autodiscover()
router = routers.DefaultRouter()
router.register(r'course', CourseViewSet)
router.register(r'assignment', AssignmentViewSet)
router.register(r'score', ScoreViewSet)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'scho ol_app.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^' + API_V1_URL, include(router.urls)),
    url(r'^' + API_V1_URL + 'oauth2/', include('provider.oauth2.urls', namespace='oauth2')),
    url(r'^api/api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)
