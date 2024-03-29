"""manatal URL Configuration

Step 2:

- Endpoint `students/` will return all students (GET) and allow student creation (POST)
- Endpoint `/schools/` will return all schools (GET) and allow school creation (POST)
- Endpoint `/schools/:id` will return the object by :id (GET) and allow editing (PUT/PATCH) or deleting (DELETE)
- Endpoint `/students/:id` will return the object by :id (GET) and allow editing (PUT/PATCH) or deleting (DELETE)

- Student creation will generate a unique identification string (like random hexadecimal or uuid4 or anything of your choice)
- Trying to add a student in a full school (maximum number of students reached) will return a DRF error message

Above requirements is implemented by override the create(), or can also hack the mixin..)

Check out the source to review OOP patterns used:
1  In: https://github.com/encode/django-rest-framework/blob/master/rest_framework/viewsets.py
2. Observe: class ModelViewSet(mixins.CreateModelMixin)
 - so create customize mixin class and use when constructing the the ViewSet object.
But for now just use the approach to overide a method in Seralizers.
See https://stackoverflow.com/questions/30650008/django-rest-framework-override-create-in-modelserializer-passing-an-extra-par

Step 3:
- Endpoint /schools/:id/students will return students who belong to school :id (GET)
- Endpoint /schools/:id/students will allow student creation in the school :id (POST)

- Endpoint /schools/:id/students/:id
- Your nested endpoint will allow GET/PUT/PATCH/DELETE methods on /schools/:id/students/:id
- Your nested endpoint will respect the same two last rules of Step 2 too

"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from rest_framework_nested import routers
from hashlib import sha1
# from school.views import DomainViewSet, NameserverViewSet  # TODO: move ViewSet classes to views.py
from school.models import Student, School

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']

class StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Student
        fields = ['url', 'first_name', 'last_name', 'school_affiliation']
    def create(self, validated_data):
        print("============")
        print(validated_data)
        school = validated_data['school_affiliation']
        if school.student_count() + 1 > school.max_student:
            # Return error b/c max number of student reached.
            raise serializers.ValidationError("Max number student reached. Current={c} Max={m}".format(c=school.student_count(), m=school.max_student))
        fname = validated_data['first_name']
        lname = validated_data['last_name']
        # Generate unique ID
        id_uniq = u'%s.%s' % (fname, lname)
        sid = sha1(id_uniq.encode('utf-8')).digest().hex()[0:20] # Could tidy up here.
        # print(sid)
        validated_data['student_ident_string'] = sid

        obj = Student.objects.create(**validated_data)
        return obj

class SchoolSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = School
        fields = ['url', 'name', 'max_student']


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
class SchoolViewSet(viewsets.ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'students', StudentViewSet)
router.register(r'schools', SchoolViewSet)

git 
router.register(r'students/<id>', StudentViewSet, basename='students')
router.register(r'schools/<id>', SchoolViewSet, basename='schools')


class StudentListViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    def get_queryset(self):
        return Student.objects.filter(school_affiliation=self.kwargs['school_pk'])

nested_router = routers.NestedSimpleRouter(router, r'schools', lookup='school')
nested_router.register(r'students', StudentListViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path(r'', include(nested_router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls'))
]
