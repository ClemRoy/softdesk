from django.urls import re_path as url
from .views import CreateUserAPIView

urlpatterns = [
    url(r'^create/$', CreateUserAPIView.as_view()),
]