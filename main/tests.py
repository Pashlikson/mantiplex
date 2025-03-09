from django.test import TestCase
from main.validators import Calculate

class Test(TestCase):
    def setUp(self):
        self.grade = Calculate.School_classVaild(2017)

    def test_School_class_validator(self):
        self.assertEqual(self.grade, 8)
