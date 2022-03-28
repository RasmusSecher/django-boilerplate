from django.urls import path
from .views import basicView

urlpatterns = [
    path("", basicView),
]
