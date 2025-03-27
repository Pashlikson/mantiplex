from django.test import TestCase

class Test(TestCase):
    def setUp(self):
        self.grade = ('')

    def test_validator(self):
        self.assertEqual(self.grade, False)
