from django.test import TestCase, Client
from django.urls import reverse


client = Client()


class TestGeodeticWorkHomeView(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        # create Work's objects

    @classmethod
    def tearDownClass(cls) -> None:
        return super().tearDownClass()

    def test_should_return_status_code_200_when_request_is_sent(self):
        expected_code = 200

        resp = client.get(reverse("geodetic-work-home"))
        actual_code = resp.status_code

        self.assertEqual(expected_code, actual_code)

    def test_should_return_correct_context_when_request_is_sent(self):
        resp = client.get(reverse("geodetic-work-home"))

        self.assertIn("works", resp.context)

    def test_should_return_correct_objects_when_request_is_sent(self):
        # list_objects = resp.context['works']
        pass
