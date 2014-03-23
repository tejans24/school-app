from rest_framework import serializers
from grades.models import Course, Assignment



class AssignmentSerializer(serializers.HyperlinkedModelSerializer):

	assignment_type = serializers.SlugRelatedField(read_only=True, slug_field='name')

	class Meta:
		model = Assignment
		fields = ['url', 'assignment_type', 'name', 'max_points', 'due_date', 'assigned_date']



class CourseSerializer(serializers.HyperlinkedModelSerializer):

	#assignments = serializers.HyperlinkedRelatedField(many=True, read_only=True ,view_name='assignment-detail')
	assignments  = AssignmentSerializer(many=True)


	class Meta:
		model = Course