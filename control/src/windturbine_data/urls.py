from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^all/', views.WindturbineDataList.as_view()),
]