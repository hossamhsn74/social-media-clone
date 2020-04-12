from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'posts'

urlpatterns = [
    path("", views.PostListView.as_view(), name="all"),
    path("new/", views.PostCreateView.as_view(), name="create"),
    url(r"by/(?P<username>[-\w]+)/$",
        views.UserPostsListView.as_view(), name="for_user"),
    url(r"by/(?P<username>[-\w]+)/(?P<pk>\d+)/$",
        views.PostDetailView.as_view(), name="single"),
    path("delete/<int:id>/", views.PostDeleteView.as_view(), name='delete'),
]
