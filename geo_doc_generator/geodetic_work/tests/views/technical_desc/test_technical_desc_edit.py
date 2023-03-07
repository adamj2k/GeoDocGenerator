from django.test import TestCase, Client
from django.urls import reverse
from geodetic_work.models.geodetic_work import GeodeticWork
from geodetic_work.models.document import TechnicalDescription
from users.models.geouser import GeoUser


client = Client()


class TestTechnicalDescrptionUpdateView(TestCase):
    def setUp(self) -> None:
        super().setUp()
        self.data = {
            "id_work": self.test_geodetic_work1.id,
            "pdf_file": "",
            "source_data": "Po analizie danych pozykanych z ODGiK ...",
            "comparision_description": "Wykonano porównanie mapy...",
            "geodetic_network_description": "Założono osnowę pomiarową ...",
            "control_survey_description": "Wykonano pomiar kontrolny ...",
            "land_survey_descrption": "Wykonano pomiar systuacyjny metodą ...",
            "results_descrption": "Wyniki uzyskano w układzie ...",
            "zudp_building_permit": "ZUD i pozwolenie na budowe ..",
            "boundary_plots": "Granice spełniają/nie spełniają ...",
            "output_documents": "Dla zamawiającego przygotowano...",
            "update_county_database": "Przekazno pliki w formacie ...",
            "update_egib_database": "Kierownik prac stwierdził/nie stwierdził ...",
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

        cls.technical_desc_work1 = TechnicalDescription.objects.create(
            id_work=cls.test_geodetic_work1,
            source_data="Akualizacja atrybutu",
            comparision_description="Wykonano porównanie mapy...",
            geodetic_network_description="Założono osnowę pomiarową ...",
            control_survey_description="Wykonano pomiar kontrolny ...",
            land_survey_descrption="Wykonano pomiar systuacyjny metodą ...",
            results_descrption="Wyniki uzyskano w układzie ...",
            zudp_building_permit="ZUD i pozwolenie na budowe ..",
            boundary_plots="Granice spełniają/nie spełniają ...",
            output_documents="Dla zamawiającego przygotowano...",
            update_county_database="Przekazno pliki w formacie ...",
            update_egib_database="Kierownik prac stwierdził/nie stwierdził ...",
        )

    @classmethod
    def tearDownClass(cls) -> None:
        return super().tearDownClass()

    def test_should_return_status_code_200_when_request_is_sent(self):
        expected_code = 200

        response = client.get(
            reverse(
                "technical-description-edit",
                kwargs={"pk": self.technical_desc_work1.pk},
            )
        )
        actual_code = response.status_code

        self.assertEqual(expected_code, actual_code)

    def test_should_update_existing_technical_descrption_object(self):
        self.client.force_login(self.test_user1)
        reponse = self.client.post(
            reverse(
                "technical-description-edit",
                kwargs={"pk": self.technical_desc_work1.pk},
            ),
            data=self.data,
        )

        self.assertEqual(reponse.status_code, 302)
        self.assertRedirects(
            reponse,
            reverse(
                "geodetic-work-details", kwargs={"pk": self.test_geodetic_work1.id}
            ),
        )
        self.technical_desc_work1.refresh_from_db()
        self.assertEqual(
            self.technical_desc_work1.source_data, self.data["source_data"]
        )

    def test_should_show_message_after_success(self):
        self.client.force_login(self.test_user1)
        reponse = self.client.post(
            reverse(
                "technical-description-edit",
                kwargs={"pk": self.technical_desc_work1.pk},
            ),
            data=self.data,
            follow=True,
        )

        self.assertContains(reponse, "Zmieniłeś dane dokumentu", status_code=200)

    def test_sholud_return_non_context_when_no_user_is_log_in(self):
        self.client.logout()
        response = client.get(
            reverse(
                "technical-description-edit",
                kwargs={"pk": self.technical_desc_work1.pk},
            )
        )

        self.assertContains(response, "Nie jesteś zalogowany", status_code=200)
