from django.urls import path
from . import views

app_name = 'groups'

urlpatterns = [
    path("", views.GroupListView.as_view(), name="all"),
    path("new/", views.GroupCreateView.as_view(), name="create"),
    path("posts/in/<slug:slug>", views.GroupDetailView.as_view(), name="single"),
]
