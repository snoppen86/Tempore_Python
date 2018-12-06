from django.test import TestCase
from TemporeApp.services.location import  get_coordinates_for_location

# Create your tests here.
TEST_LOCATION = "backluraskolan"
class LocationServiceTest(TestCase):

    def test_get_location_coordinates(self):
        resp = get_coordinates_for_location(TEST_LOCATION)
        self.assertIsNotNone(resp)

