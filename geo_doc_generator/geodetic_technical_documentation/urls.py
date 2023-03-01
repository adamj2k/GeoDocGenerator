from django.urls import path
from geodetic_technical_documentation.views.technical_desc.views import (
    TechnicalDescriptionGeneratePdf,
    TechnicalDescriptionPdfPreview,
)
from geodetic_technical_documentation.views.network_coordinates.views import (
    GeodeticNetworkCoordinatesGeneratePDF,
    GeodeticNetworkCoordinatesPdfPreview,
)
from geodetic_technical_documentation.views.network_survey.views import (
    GeodeticNetworkSurveysGeneratePDF,
    GeodeticNetworkSurveyPdfPreview,
)
from geodetic_technical_documentation.views.list_coordinates.views import (
    ListOfCoordinatesGeneratePDF,
    ListOfCoordinatesGeneratePdfPreview,
)
from geodetic_technical_documentation.views.table_of_content.views import (
    TableOfContentGenerate,
    TableOfContentPreView,
)
from geodetic_technical_documentation.views.generate_merge_pdf.views import (
    GeodeticWorkDocumentsPDFGenerate,
)

urlpatterns = [
    path(
        "techdesc/<int:pk>",
        TechnicalDescriptionGeneratePdf.as_view(),
        name="technical-discription-generate",
    ),
    path(
        "techdescpreview/<int:pk>",
        TechnicalDescriptionPdfPreview.as_view(),
        name="technical-discription-preview",
    ),
    path(
        "geodeticnetsurv/<int:pk>",
        GeodeticNetworkSurveysGeneratePDF.as_view(),
        name="network-survey-generate",
    ),
    path(
        "geodeticnetsurvpreviwe/<int:pk>",
        GeodeticNetworkSurveyPdfPreview.as_view(),
        name="network-survey-preview",
    ),
    path(
        "geodeticnetcoor/<int:pk>",
        GeodeticNetworkCoordinatesGeneratePDF.as_view(),
        name="network-coordinates-generate",
    ),
    path(
        "geodeticnetcoorpreview/<int:pk>",
        GeodeticNetworkCoordinatesPdfPreview.as_view(),
        name="network-coordinates-preview",
    ),
    path(
        "listcoord/<int:pk>",
        ListOfCoordinatesGeneratePDF.as_view(),
        name="list-coordinates-generate",
    ),
    path(
        "listcoordpreview/<int:pk>",
        ListOfCoordinatesGeneratePdfPreview.as_view(),
        name="list-coordinates-preview",
    ),
    path(
        "tocgenerate/<int:pk>",
        TableOfContentGenerate.as_view(),
        name="table-of-content-generate",
    ),
    path(
        "tocpreview/<int:pk>",
        TableOfContentPreView.as_view(),
        name="table-of-content-preview",
    ),
    path(
        "geodocgenerate/<int:pk>",
        GeodeticWorkDocumentsPDFGenerate.as_view(),
        name="geo-doc-pdf-generator",
    ),
]
