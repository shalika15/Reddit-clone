from django.conf.urls import url
from . import views

app_name = "create"

urlpatterns = [
    url('create/', views.create, name="create"),
    url(r'(?P<pk1>[0-9]+)/upvote' ,views.upvote, name = 'uvote' ),
    url(r'(?P<pk2>[0-9]+)/downvote' ,views.downvote, name = 'dvote' ),
]
