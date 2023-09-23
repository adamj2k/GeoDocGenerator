from django.test import TestCase, Client
from django.urls import reverse
from geodetic_work.models.geodetic_work import GeodeticWork
from users.models.geouser import GeoUser


client = Client()


class TestGeodeticWorkCreateView(TestCase):
    def setUp(self) -> None:
        super().setUp()
        self.data = {
            "id_work": "6640.111.2023",
            "voivodeship": "zachodniopomorskie",
            "county": "Police",
            "commune": "Police",
            "precinct": "1094",
            "work_object": "Police, ul. Biała 12",
            "plots": "1, 2",
            "work_scope": "MDCP",
            "survey_date": "2023-02-12",
            "begin_date": "2023-02-01",
            "area": "1 ha",
            "change_bdot_database": False,
            " change_gesut_database": False,
            "change_egib_database": True,
            "documentation_date": "2023-02-12",
            "status": "INP",
        }

    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        cls.test_user1 = GeoUser.objects.create(
            username="testuser1", email="testuser1@test.in", password="secret"
        )

    @classmethod
    def tearDownClass(cls) -> None:
        return super().tearDownClass()

    def test_should_return_status_code_200_when_request_is_sent(self):
        expected_code = 200

        response = client.get(reverse("geodetic-work-create"))
        actual_code = response.status_code

        self.assertEqual(expected_code, actual_code)

    def test_should_create_geodetic_work_object(self):
        reponse = self.client.post(
            reverse("geodetic-work-create"), data=self.data, follow=True
        )

        self.assertEqual(reponse.status_code, 200)
        self.assertEqual(
            GeodeticWork.objects.filter(id_work="6640.111.2023").count(), 1
        )

    def test_should_redirect_to_proper_url_after_success(self):
        reponse = self.client.post(
            reverse("geodetic-work-create"), data=self.data, follow=True
        )

        self.assertRedirects(
            reponse,
            "/",
            status_code=302,
            target_status_code=200,
            fetch_redirect_response=True,
        )

    def test_sholud_return_non_context_when_no_user_is_log_in(self):
        self.client.logout()
        response = client.get(reverse("geodetic-work-create"))

        self.assertContains(response, "Nie jesteś zalogowany", status_code=200)
