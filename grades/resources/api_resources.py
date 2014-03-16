from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from tastypie import fields
from tastypie.http import HttpGone

__author__ = 'tejawork'
from tastypie.resources import ModelResource
from tastypie.authorization import Authorization
from accounts.resources.api_resources import StudentResource
from grades.models.assignment import Assignment
from grades.models.course import Course
from grades.models.score import Score
from grades.models.assignment_type import AssignmentType
from django.conf.urls import url
from tastypie.utils import trailing_slash
from tastypie.http import HttpMultipleChoices
from tastypie.bundle import Bundle


class AssignmentResource(ModelResource):

    def get_resource_uri(self, bundle_or_obj=None):

        kwargs = {
            'api_name': 'v1',
            'resource_name': self._meta.resource_name,
            }

        return self._build_reverse_url('api_dispatch_detail', kwargs=kwargs)

    class Meta:
        queryset = Assignment.objects.all()
        resource_name = 'assignment'
        authorization = Authorization()


class AssignmentTypeResource(ModelResource):

    class Meta:
        queryset = AssignmentType.objects.all()
        authorization = Authorization()
        resource_name = 'assignment_type'
        include_resource_uri = False


class CourseResource(ModelResource):

    assignment_types = fields.ToManyField(AssignmentTypeResource, 'assignment_types',
                                          null=True, blank=True, full=True)

    assignments = fields.ToManyField(AssignmentResource, 'assignments', null=True, full=True)
    students = fields.ManyToManyField(StudentResource, 'students', null=True, full=True)

    def prepend_urls(self):

        return [
            url(r"^(?P<resource_name>%s)/(?P<pk>\w[\w/-]*)/assignment%s$" % (self._meta.resource_name,
                trailing_slash()), self.wrap_view('get_assignment_list'), name="api_get_assignment_list"),

            url(r"^(?P<resource_name>%s)/(?P<pk>\w[\w/-]*)/assignment/(?P<assignment_slug>[^/]+)%s$" %
                (self._meta.resource_name,
                trailing_slash()), self.wrap_view('get_assignment_detail'), name="api_get_assignment_detail"),
        ]

    def get_assignment_list(self, request, **kwargs):
        try:
            bundle = self.build_bundle(data={'pk': kwargs['pk']}, request=request)
            obj = self.cached_obj_get(bundle=bundle, **self.remove_api_resource_names(kwargs))
        except ObjectDoesNotExist:
            return HttpGone()
        except MultipleObjectsReturned:
            return HttpMultipleChoices("More than one resource is found at this URI.")

        assignment_resource = AssignmentResource()
        return assignment_resource.get_list(request, p_id=obj.id)

    def get_assignment_detail(self, request, assignment_slug=None, **kwargs):

        try:
            bundle = self.build_bundle(data={'pk': kwargs['pk']}, request=request)
            obj = self.cached_obj_get(bundle=bundle, **self.remove_api_resource_names(kwargs))
        except ObjectDoesNotExist:
            return HttpGone()
        except MultipleObjectsReturned:
            return HttpMultipleChoices("More than one resource is found at this URI.")

        nested_resource = AssignmentResource()
        return nested_resource.get_detail(request, p_id=obj.id, slug=assignment_slug)

    class Meta:
        queryset = Course.objects.all()
        resource_name = 'course'
        authorization = Authorization()


class ScoreResource(ModelResource):

    class Meta:
        queryset = Score.objects.all()
        resource_name = 'score'
        authorization = Authorization()
