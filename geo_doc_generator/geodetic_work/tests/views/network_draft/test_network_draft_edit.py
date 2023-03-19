from django.test import TestCase, Client
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from geodetic_work.models.geodetic_work import GeodeticWork
from geodetic_work.models.document import GeodeticNetworkDraft
from users.models.geouser import GeoUser


client = Client()


class TestGeodeticNetworkDraftEditView(TestCase):
    def setUp(self) -> None:
        super().setUp()
        self.test_file = SimpleUploadedFile(
            "test_file.pdf", b"file content", content_type="application/pdf"
        )
        self.data = {"id_work": self.test_geodetic_work1.id, "pdf_file": self.test_file}

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

        cls.test_geodetic_network_darft1 = GeodeticNetworkDraft.objects.create(
            id_work=cls.test_geodetic_work1,
            pdf_file="05_2Szkice_BON_GESUT-Model-000.pdf",
        )

    @classmethod
    def tearDownClass(cls) -> None:
        return super().tearDownClass()

    def tearDown(self) -> None:
        return super().tearDown()

    def test_should_return_status_code_200_when_request_is_sent(self):
        expected_code = 200

        response = client.get(
            reverse("network-draft-edit", kwargs={"pk": self.test_geodetic_work1.pk})
        )
        actual_code = response.status_code

        self.assertEqual(expected_code, actual_code)

    def test_should_update_existing_object_geodetic_network_draft(self):
        expected_file = SimpleUploadedFile(
            "test_file.pdf", b"file content", content_type="application/pdf"
        )
        expected_file_content = expected_file.read()
        self.client.force_login(self.test_user1)
        response = client.post(
            reverse("network-draft-edit", kwargs={"pk": self.test_geodetic_work1.pk}),
            data=self.data,
        )

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(
            response,
            reverse(
                "geodetic-work-details", kwargs={"pk": self.test_geodetic_work1.id}
            ),
        )
        self.test_geodetic_network_darft1.refresh_from_db()
        self.assertEqual(
            self.test_geodetic_network_darft1.pdf_file.read(), expected_file_content
        )

    def test_should_show_message_after_success(self):
        self.client.force_login(self.test_user1)
        response = client.post(
            reverse("network-draft-edit", kwargs={"pk": self.test_geodetic_work1.pk}),
            data=self.data,
            follow=True,
        )

        self.assertContains(response, "Zmieniłeś dane dokumentu", status_code=200)

    def test_should_non_contex_when_no_user_is_log_in(self):
        self.client.logout()
        response = client.get(
            reverse("network-draft-edit", kwargs={"pk": self.test_geodetic_work1.pk})
        )

        self.assertContains(response, "Nie jesteś zalogowany", status_code=200)
