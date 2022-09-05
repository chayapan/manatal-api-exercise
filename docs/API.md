
- Endpoint `students/` will return all students (GET) and allow student creation (POST)
- Endpoint `/schools/` will return all schools (GET) and allow school creation (POST)
- Endpoint `/schools/:id` and `/students/:id` will return the object by :id (GET) and allow editing (PUT/PATCH) or deleting (DELETE)
- Student creation will generate a unique identification string (like random hexadecimal or uuid4 or anything of your choice)
- Trying to add a student in a full school (maximum number of students reached) will return a DRF error message




- ModelViewSet: [https://www.django-rest-framework.org/api-guide/viewsets/#modelviewset](https://www.django-rest-framework.org/api-guide/viewsets/#modelviewset)
- ModelSerializer: [https://www.django-rest-framework.org/api-guide/serializers/#modelserializer](https://www.django-rest-framework.org/api-guide/serializers/#modelserializer)
- drf-nested-routers: https://github.com/alanjds/drf-nested-routers

### Django Nested Routers

- Endpoint /schools/:id/students will return students who belong to school :id (GET)
- Endpoint /schools/:id/students will allow student creation in the school :id (POST)
- Your nested endpoint will allow GET/PUT/PATCH/DELETE methods on /schools/:id/students/:id
- Your nested endpoint will respect the same two last rules of Step 2 too


### Filter, Faker, Pagination


- You can add fields of your choice to students and schools such as location, nationality, age, etc. You can use the Python Faker library to generate random data (names, etc) to populate fields.
- You can add search filters to your endpoints such as /students/?search=jeremy and you can add ordering filters as well, for example by age, by nationality, etc.
- You can add pagination or anything else that you wanna show us, feel free to add interesting stuff to this project!




### Test

1. Create School entity first.
2. Create Student entity and make affiliate with a school.


http://127.0.0.1:8000/

Shows API page.


User List
http://127.0.0.1:8000/users/

Student List
http://127.0.0.1:8000/students/

School List
http://127.0.0.1:8000/schools/

School Instance
http://127.0.0.1:8000/schools/1/


Nested path
http://127.0.0.1:8000/schools/1/students/