from django.urls import path, re_path
from . import views

urlpatterns = [
	path("", views.Login, name="Auth"),
	path("login/", views.Login, name="Login"),
	path("logout/", views.Logout, name="Logout"),
	path("register/", views.Register, name="Register"),
]
