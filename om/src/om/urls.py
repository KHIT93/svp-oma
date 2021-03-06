"""O&M URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))

Including API viewsets
    1. Add an import: from other_app.views import MyAppAPIViewset
    2. Register the endpoint with the router: router.register(r'myapp-endpoint', MyAppAPIViewset)
    3. If method get_queryset is defined on the ViewSet change the router registration like this: router.register(r'myapp-endpoint', MyAppAPIViewset, 'MyModel')
"""
from django.conf.urls import url, include
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from dashboard.views.dashboard_view import DashboardView
#Rest framework imports
from rest_framework import routers
from appcore.views.user_view_set import UserViewSet
from appcore.views.group_view_set import GroupViewSet
from appcore.views.audit_log_viewset import AuditLogViewset
from errors.views.error_code_api_viewset import ErrorCodeAPIViewset
from turbinemanagement.views.windfarm_api_viewset import WindfarmAPIViewset
from turbinemanagement.views.windturbine_api_viewset import WindturbineAPIViewset
from turbinemanagement.views.windturbine_data_api_viewset import WindturbineDataAPIViewset
from turbinemanagement.views.windturbine_error_api_viewset import WindturbineErrorAPIViewset
from turbinemanagement.views.windturbine_setting_api_viewset import WindturbineSettingAPIViewset
from turbinemanagement.views.windfarm_api_viewset import WindfarmWithRelationshipsAPIView
from turbinemanagement.views.windfarm_api_viewset import WindfarmWithNestedRelationshipsAPIView
from turbinemanagement.views.windturbine_api_viewset import WindturbineWithRelationshipsAPIView

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'auditlog', AuditLogViewset)
router.register(r'errors', ErrorCodeAPIViewset)
router.register(r'windfarms', WindfarmAPIViewset)
router.register(r'windturbines', WindturbineAPIViewset)
router.register(r'windturbine-data', WindturbineDataAPIViewset, 'WindTurbineData')
router.register(r'windturbine-errors', WindturbineErrorAPIViewset, 'WindTurbineError')
router.register(r'windturbine-settings', WindturbineSettingAPIViewset, 'WindTurbineSettings')

urlpatterns = [
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^$', login_required(DashboardView.as_view())),
    url(r'^webapi/windfarms/simple/', WindfarmWithRelationshipsAPIView.as_view()),
    url(r'^webapi/windfarms/complete/', WindfarmWithNestedRelationshipsAPIView.as_view()),
    url(r'^webapi/windturbines/complete/', WindturbineWithRelationshipsAPIView.as_view()),
    url(r'^webapi/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
