from django.test import TestCase, Client
from django.urls import reverse
from geodetic_work.models.geodetic_work import GeodeticWork
from users.models.geouser import GeoUser


client = Client()


class TestGeodeticWorkCreateView(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        return super().setUpClass()

    def tearDown(self) -> None:
        return super().tearDown()

    def test_should_return_status_code_200_when_request_is_sent(self):
        pass

    def test_should_update_existing_geodetic_work_object(self):
        pass

    def test_should_redirect_to_proper_url_after_success_editing(self):
        pass
