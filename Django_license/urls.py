"""Django_license URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
"""
from django.conf.urls import url
from django.contrib import admin

from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from Django_license import views
from user.views import StbViewSet, PhysicalViewSet, getStbFunction

# stb_list = StbViewSet.as_view({
#   'get': 'recent_user',
#   'post': 'user_ch_list'
# })

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'stbs', StbViewSet)
router.register(r'phystbs', PhysicalViewSet)
#router.register(r'get_stb_ch', getStbFunction, base_name='get_stb_ch')


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^rest-swagger/', views.schema_view),
    url(r'^get-stb-ch/', getStbFunction),
    url(r'^', include(router.urls))
]
