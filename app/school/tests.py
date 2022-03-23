from django.test import TestCase
from school import models
# - Students have a first name, the last name, and a student identification string (20 characters max for each)
# - Schools have a name (20 char max) and a maximum number of students (any positive integer)
# - Each student object must belong to a school object

class StudentCreationTestCase(TestCase):
    def setUp(self):
        models.School.objects.create(name="example")
        models.School.objects.create(name="example__________________________________________name")
    def test_animals_can_speak(self):
        """Animals that can speak are correctly identified"""
        lion = Animal.objects.get(name="lion")
        cat = Animal.objects.get(name="cat")
        self.assertEqual(lion.speak(), 'The lion says "roar"')
        self.assertEqual(cat.speak(), 'The cat says "meow"')

class SchoolManagementTestCase(TestCase):
    def setUp(self):
        Animal.objects.create(name="lion", sound="roar")
        Animal.objects.create(name="cat", sound="meow")

    def test_animals_can_speak(self):
        """Animals that can speak are correctly identified"""
        lion = Animal.objects.get(name="lion")
        cat = Animal.objects.get(name="cat")
        self.assertEqual(lion.speak(), 'The lion says "roar"')
        self.assertEqual(cat.speak(), 'The cat says "meow"')