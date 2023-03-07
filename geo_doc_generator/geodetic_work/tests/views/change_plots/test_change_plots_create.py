from django.test import TestCase, Client
from django.urls import reverse
from geodetic_work.models.geodetic_work import GeodeticWork
from geodetic_work.models.document import ChangeListPlot
from users.models.geouser import GeoUser


client = Client()


class TestChangeListPlotCreateView(TestCase):
    def setUp(self) -> None:
        super().setUp()
        self.data = {}

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
        pass

    def test_should_create_new_object_geodetic_network_survey(self):
        pass

    def test_should_show_message_after_success(self):
        pass

    def test_should_non_contex_when_no_user_is_log_in(self):
        pass
