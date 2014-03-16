from django.conf.urls import patterns, include, url
from django.contrib import admin
from tastypie.api import Api
from accounts.resources.api_resources import StudentResource, UserResource
from grades.resources.api_resources import AssignmentResource, CourseResource, ScoreResource, AssignmentTypeResource

API_V1_URL = 'api/v1/'

admin.autodiscover()

v1_api = Api(api_name='v1')
v1_api.register(UserResource())
v1_api.register(StudentResource())
v1_api.register(CourseResource())

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'scho ol_app.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(v1_api.urls)),
    url(r'^' + API_V1_URL + 'oauth2/', include('provider.oauth2.urls', namespace='oauth2')),
    url(r'^' + API_V1_URL + 'doc/', include('tastypie_swagger.urls', namespace='tastypie_swagger')),
)
