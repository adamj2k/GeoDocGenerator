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

    def test_should_return_status_code_201_when_request_is_sent(self):
        pass

    def test_should_create_geodetic_work_object(self):
        pass

    def test_should_redirect_to_proper_url_after_success(self):
        pass

    def test_sholud_return_non_context_when_no_user_is_log_in(self):
        pass
