from django.urls import path
from .views import basicView, dataView, downloadView

urlpatterns = [
    path("", basicView),
    path("data/", dataView),
    path("download/", downloadView, name="download"),
]
