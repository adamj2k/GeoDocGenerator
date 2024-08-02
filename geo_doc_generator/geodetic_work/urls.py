from django.urls import path
from geodetic_work.views.geodetic_work.views import (
    GeodeticWorkCreatView,
    GeodeticWorkDetailsView,
    GeodeticWorkEditView,
    GeodeticWorkHome,
    GeodeticWorkListView,
)
from geodetic_work.views.technical_desc.views import (
    TechnicalDescriptionCreateView,
    TechnicalDescriptionUpdateView,
)
from geodetic_work.views.comparision_map.views import (
    ComparisionMapCreateView,
    ComparisionMapUpdateView,
)
from geodetic_work.views.network_survey.views import (
    GeodeticNetworkSurveyCreateView,
    GeodeticNetworkSurveyUpdateView,
)
from geodetic_work.views.network_draft.views import (
    GeodeticNetworkDraftCreateView,
    GeodeticNetworkDraftUpdateView,
)
from geodetic_work.views.network_coordinates.views import (
    NetworkCoordinatesCreateView,
    NetworkCooridnatesUpdateView,
)
from geodetic_work.views.field_draft.views import (
    FieldDraftCreateView,
    FieldDraftUpdateView,
)
from geodetic_work.views.list_coordinates.views import (
    ListCoordinatesCreateView,
    ListCoordinatesUpdateView,
)
from geodetic_work.views.change_building.views import (
    ChangeBuildingCreateView,
    ChangeBuildingUpdateView,
    ChangeBuildingDeleteView,
)
from geodetic_work.views.change_plots.views import (
    ChangePlotsCreateView,
    ChangePlotsUpdateView,
)

urlpatterns = [
    path("", GeodeticWorkHome.as_view(), name="geodetic-work-home"),
    path("worklist/", GeodeticWorkListView.as_view(), name="geodetic-work-list"),
    path("workcreate/", GeodeticWorkCreatView.as_view(), name="geodetic-work-create"),
    path(
        "workdetails/<int:pk>",
        GeodeticWorkDetailsView.as_view(),
        name="geodetic-work-details",
    ),
    path(
        "workedit/<int:pk>", GeodeticWorkEditView.as_view(), name="geodetic-work-edit"
    ),
    path(
        "workdetails/<int:pk>/techdesccreate/",
        TechnicalDescriptionCreateView.as_view(),
        name="technical-description-create",
    ),
    path(
        "techdescedit/<int:pk>",
        TechnicalDescriptionUpdateView.as_view(),
        name="technical-description-edit",
    ),
    path(
        "workdetails/<int:pk>/comparisionmapcreate/",
        ComparisionMapCreateView.as_view(),
        name="comparision-map-create",
    ),
    path(
        "comparisionmapedit/<int:pk>",
        ComparisionMapUpdateView.as_view(),
        name="comparision-map-edit",
    ),
    path(
        "workdetails/<int:pk>/networksurveycreate/",
        GeodeticNetworkSurveyCreateView.as_view(),
        name="network-survey-create",
    ),
    path(
        "networksurveyedit/<int:pk>",
        GeodeticNetworkSurveyUpdateView.as_view(),
        name="network-survey-edit",
    ),
    path(
        "workdetails/<int:pk>/networkdraftcreate/",
        GeodeticNetworkDraftCreateView.as_view(),
        name="network-draft-create",
    ),
    path(
        "networkdraft/<int:pk>",
        GeodeticNetworkDraftUpdateView.as_view(),
        name="network-draft-edit",
    ),
    path(
        "workdetails/<int:pk>/networkcoordinatescreate/",
        NetworkCoordinatesCreateView.as_view(),
        name="network-coordinates-create",
    ),
    path(
        "networkcoordinates/<int:pk>",
        NetworkCooridnatesUpdateView.as_view(),
        name="network-coordinates-edit",
    ),
    path(
        "workdetails/<int:pk>/fielddraftcreate/",
        FieldDraftCreateView.as_view(),
        name="field-draft-create",
    ),
    path(
        "fielddraft/<int:pk>", FieldDraftUpdateView.as_view(), name="field-draft-edit"
    ),
    path(
        "workdetails/<int:pk>/listcoordinatescreate/",
        ListCoordinatesCreateView.as_view(),
        name="list-coordinates-create",
    ),
    path(
        "listcoordinates/<int:pk>",
        ListCoordinatesUpdateView.as_view(),
        name="list-coordinates-edit",
    ),
    path(
        "workdetails/<int:pk>/changebuildingscreate/",
        ChangeBuildingCreateView.as_view(),
        name="change-buildings-create",
    ),
    path(
        "changebuildings/<int:pk>",
        ChangeBuildingUpdateView.as_view(),
        name="change-buildings-edit",
    ),
    path(
        "deletebuildings/<int:pk>",
        ChangeBuildingDeleteView.as_view(),
        name="change-buildings-delete",
    ),
    path(
        "workdetails/<int:pk>/changeplotscreate/",
        ChangePlotsCreateView.as_view(),
        name="change-plots-create",
    ),
    path(
        "changeplots/<int:pk>",
        ChangePlotsUpdateView.as_view(),
        name="change-plots-edit",
    ),
]
