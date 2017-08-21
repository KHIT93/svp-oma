from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^all/', views.WindturbineSettingDetail.as_view()),
    url(r'^update/(?P<pk>[0-9]+)/$', views.WindturbineSettingDetail.as_view()),
]