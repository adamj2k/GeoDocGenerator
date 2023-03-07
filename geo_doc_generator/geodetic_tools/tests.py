from django.test import TestCase, Client
from django.urls import reverse

client = Client()


class TestHighConversionView(TestCase):
    def setUp(self) -> None:
        super().setUp()

    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()

    @classmethod
    def tearDownClass(cls) -> None:
        return super().tearDownClass()

    def test_should_return_status_code_200_when_request_is_sent(self):
        pass

    def test_should_create_new_object_geodetic_network_survey(self):
        pass

    def test_should_show_message_after_success(self):
        pass

    def test_should_non_contex_when_no_user_is_log_in(self):
        pass
