from django.urls import path
from . import views

urlpatterns = [
	path("", views.index, name="index"),
	path("create/", views.ContactCreate.as_view(), name="create"),
	path("delete/<slug:id>/", views.ContactDelete.as_view(), name="delete"),
	path("update/<slug:id>/", views.ContactUpdate.as_view(), name="update"),
]