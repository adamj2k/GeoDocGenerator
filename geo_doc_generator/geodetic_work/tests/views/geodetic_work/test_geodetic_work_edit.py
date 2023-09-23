from django.test import TestCase, Client
from django.urls import reverse
from geodetic_work.models.geodetic_work import GeodeticWork
from users.models.geouser import GeoUser


client = Client()


class TestGeodeticWorkEditView(TestCase):
    def setUp(self) -> None:
        super().setUp()
        self.data = {
            "id_work": "6640.222.2023",
            "voivodeship": "zachodniopomorskie",
            "county": "Police",
            "commune": "Police",
            "precinct": "1094",
            "work_object": "Police, ul. Biała 12",
            "plots": "1, 2",
            "work_scope": "MDCP",
            "survey_date": "2023-02-12",
            "begin_date": "2023-02-01",
            "area": "1.50 ha",
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

        cls.test_geodetic_work1 = GeodeticWork.objects.create(
            contractor=cls.test_user1,
            id_work="6640.222.2023",
            voivodeship="zachodniopomorskie",
            county="Szczecin",
            commune="Szczecin",
            precinct="1094",
            work_object="Szczecin, ul. Czarna 12",
            plots="123, 124",
            work_scope="MDCP",
            survey_date="2023-01-12",
            begin_date="2023-01-01",
            area="111 ha",
            change_bdot_database=False,
            change_gesut_database=False,
            change_egib_database=True,
            documentation_date="2023-01-12",
            status="INP",
        )

    @classmethod
    def tearDownClass(cls) -> None:
        return super().tearDownClass()

    def test_should_return_status_code_200_when_request_is_sent(self):
        expected_code = 302

        response = client.post(
            reverse("geodetic-work-edit", kwargs={"pk": self.test_geodetic_work1.pk}),
            data=self.data,
        )
        actual_code = response.status_code

        self.assertEqual(expected_code, actual_code)

    def test_should_update_existing_geodetic_work_object(self):
        self.client.force_login(self.test_user1)
        response = client.post(
            reverse("geodetic-work-edit", kwargs={"pk": self.test_geodetic_work1.pk}),
            data=self.data,
        )

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("geodetic-work-home"))
        self.test_geodetic_work1.refresh_from_db()
        self.assertEqual(self.test_geodetic_work1.id_work, self.data["id_work"])
        self.assertEqual(self.test_geodetic_work1.area, self.data["area"])

    def test_should_show_message_after_success_editing(self):
        self.client.force_login(self.test_user1)
        response = client.post(
            reverse("geodetic-work-edit", kwargs={"pk": self.test_geodetic_work1.pk}),
            data=self.data,
            follow=True,
        )

        self.assertContains(response, "Zaktualizowałeś dane pracy o id")
