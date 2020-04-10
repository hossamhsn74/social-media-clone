from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path("", views.PostListView.as_view(), name="all"),
    path("new/", views.PostCreateView.as_view(), name="create"),
    path("by/<username:username>",
         views.UserPostsListView.as_view(), name="for_user"),
    path('by/<username:username>/<pk:pk>/',
         views.PostDetailView.as_view(), name='single'),
    path("delete/<int:id>/", views.PostDeleteView.as_view(), name='delete'),
]
