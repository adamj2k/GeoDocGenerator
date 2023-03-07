from django.test import TestCase, Client
from django.urls import reverse
from geodetic_work.models.geodetic_work import GeodeticWork
from geodetic_work.models.document import GeodeticNetworkCoordinates
from users.models.geouser import GeoUser


client = Client()


class TestGeodeticCoordinatesCreateView(TestCase):
    def setUp(self) -> None:
        super().setUp()
        self.data = {
            "id_work": self.test_geodetic_work1.id,
            "list_of_coordinates": "lista wspolrzednych",
            "pdf_file": "",
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
    def tearDownClass(cls) -> None:
        return super().tearDownClass()

    def test_should_return_status_code_200_when_request_is_sent(self):
        expected_code = 200
        response = client.get(
            reverse(
                "network-coordinates-create", kwargs={"pk": self.test_geodetic_work1.pk}
            )
        )
        actual_code = response.status_code

        self.assertEqual(expected_code, actual_code)

    def test_should_create_new_object_geodetic_list_coordinates(self):
        response = client.post(
            reverse(
                "network-coordinates-create", kwargs={"pk": self.test_geodetic_work1.pk}
            ),
            data=self.data,
        )

        self.assertEqual(response.status_code, 302)
        self.assertEqual(
            GeodeticNetworkCoordinates.objects.filter(
                list_of_coordinates="lista wspolrzednych"
            ).count(),
            1,
        )

    def test_should_show_message_after_success(self):
        pass

    def test_should_non_contex_when_no_user_is_log_in(self):
        pass
