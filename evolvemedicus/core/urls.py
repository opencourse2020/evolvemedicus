from django.conf.urls import url
from django.urls import path, include

from . import views


app_name = "core"


urlpatterns = [
	path("", views.HomeView.as_view(), name="dashboard"),

]
