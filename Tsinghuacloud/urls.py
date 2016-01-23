"""Tsinghuacloud URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from SitePages import views as SiteViews
from ApiLayer import urls as ceilometer_api_interface
from AlarmNotification import views as AlarmNotice

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(ceilometer_api_interface)),
    url(r'^overview/health/$', SiteViews.overview, name="Overview | Health"),
    url(r'^overview/resources/$', SiteViews.resource_page, name="Overview | Resource Overview"),
    url(r'^overview/topology/$', SiteViews.netTopo_page, name="Overview | Network Topology"),
    url(r'^monitor/meters/$', SiteViews.meters_page, name="Monitor | Meter Overview"),
    url(r'^monitor/alarms/create-alarm/$', SiteViews.createAlarm_page, name="Monitor | Alarms | Create New Alarm"),
    url(r'^test/$', SiteViews.test_page, name="Test Page"),
    url(r'^alarm-notice/$', AlarmNotice.notification, name="createAlarm Page"),
    url(r'^$', SiteViews.overview, name="Overview Page"),
]
