from . import views
from django.conf.urls import url

app_name = "Accountt"

urlpatterns = [
    url('signup/', views.signup, name="signup"),
    url('login/', views.logins, name="login"),
]
