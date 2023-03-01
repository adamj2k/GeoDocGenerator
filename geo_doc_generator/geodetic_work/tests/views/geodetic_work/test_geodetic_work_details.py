from django.test import TestCase, Client
from django.urls import reverse
from geodetic_work.models.geodetic_work import GeodeticWork
from users.models.geouser import GeoUser

client = Client()


class TestGeodeticWorkDetailView(TestCase):
    @classmethod
    def setUpClass(cls):
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
            work_scope="sporządzenie mapy do celów projektowych",
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
    def tearDownClass(cls):
        return super().tearDownClass()

    def test_should_return_status_code_200_when_request_is_sent(self):
        expected_code = 200

        resp = client.get(
            reverse("geodetic-work-details", kwargs={"pk": self.test_geodetic_work1.id})
        )
        actual_code = resp.status_code

        self.assertEqual(expected_code, actual_code)

    def test_should_return_correct_context_when_request_is_sent(self):
        resp = client.get(
            reverse("geodetic-work-details", kwargs={"pk": self.test_geodetic_work1.id})
        )

        self.assertIn("work", resp.context)

    def test_should_return_correct_objects_when_request_is_sent(self):
        self.client.login(username="testuser1", password="secret")
        response = self.client.get(
            reverse("geodetic-work-details", kwargs={"pk": self.test_geodetic_work1.id})
        )
        object_work = response.context["work"]

        self.assertEqual(object_work, self.test_geodetic_work1)
        self.assertTemplateUsed(response, "geodetic_work/geodetic_work_details.html")
        self.assertEqual(response.status_code, 200)
