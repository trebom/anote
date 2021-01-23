from django.urls import path
from notes import views as note_views

app_name = "core"

urlpatterns = [
    path("", note_views.HomeView.as_view(), name="home")
]
