from django.urls import path

from .views import (aboutView, addFlavor, deleteFlavor, healthCheck,
                    jellybeanFlavorView, updateFlavor)

urlpatterns = [
    path("", jellybeanFlavorView, name="jellybeans"),
    path("create/", addFlavor, name="addflavor"),
    path("delete/<int:flavorId>/", deleteFlavor, name="deleteflavor"),
    path("update/<int:flavorId>/", updateFlavor, name="updateflavor"),
    path("about", aboutView, name="about"),
    path("health/", healthCheck, name="healthcheck"),
]