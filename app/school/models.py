from django.db import models

# Create your models here.
# Add models to create the following structure:
# - Students have a first name, the last name, and a student identification string (20 characters max for each)
# - Schools have a name (20 char max) and a maximum number of students (any positive integer)
# - Each student object must belong to a school object

class School(models.Model):
    name = models.CharField(max_length=20)
    max_student = models.IntegerField()
    # TODO: validate with MinValueValidator

class Student(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    student_ident_string = models.CharField(max_length=20)
    school_affiliation = models.ForeignKey(School, on_delete=models.CASCADE)
    # TODO: check delete constraint

    
