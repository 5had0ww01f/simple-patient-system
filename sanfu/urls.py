"""sanfu URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django.conf.urls import url
from django.contrib.auth.views import login

from appointment.views import appointment_index
from infomanage.views import infomanage_index
from clinic.views import clinic_index
from pharmacy.views import pharmacy_index
from database.views import addPatient
from dashboard.views import dashboard_index, google_check

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/', login),
    path('appointment/', appointment_index),
    path('index/', dashboard_index),
    path('infomanage/', infomanage_index),
    path('database/', addPatient),
    url(r'^clinic/(.+)/$', clinic_index),
    path('pharmacy/', pharmacy_index),
    path('google9eb2f55447b43980.html', google_check),
    path('', dashboard_index),
]
