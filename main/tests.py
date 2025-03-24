from django.test import TestCase
from main.utils import validate_profile_form

class Test(TestCase):
    def setUp(self):
        self.grade = validate_profile_form('')

    def test_validator(self):
        self.assertEqual(self.grade, False)
