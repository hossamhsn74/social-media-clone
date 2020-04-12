from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomePage.as_view(), name='homepage'),
    path('accounts/', include('accounts.urls'), name='accounts'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('thanks/', views.thanksView.as_view(), name='thanks'),
    path('test/', views.testView.as_view(), name='test'),
    path('groups/', include('groups.urls'), name='groups'),
    path('posts/', include('posts.urls'), name='posts'),
]
