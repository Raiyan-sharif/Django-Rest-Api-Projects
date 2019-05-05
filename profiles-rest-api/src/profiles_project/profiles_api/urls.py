from django.conf.urls import url
from .views import HelloApiView

urlpatterns = [
    url(r'^hello-view/',HelloApiView.as_view()),
]

