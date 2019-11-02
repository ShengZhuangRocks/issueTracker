from django.urls import path
from .views import log_in, sign_up, log_out

app_name = "accounts"

urlpatterns = [
    path("signup/", sign_up, name="signup"),
    path("login/", log_in, name="login"),
    path("logout/", log_out, name="logout"),
]