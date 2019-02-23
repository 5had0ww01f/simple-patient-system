"""sanfu URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView
from django.contrib import admin
from appointment.views import appointment_index
from infomanage.views import infomanage_index
from clinic.views import clinic_index
from pharmacy.views import pharmacy_index
from database.views import addPatient
from dashboard.views import dashboard_index

urlpatterns = [
    url(r'^accounts/login/$', LoginView.as_view()),
    url(r'^admin/', admin.site.urls),
    url(r'^appointment/', appointment_index),
    url(r'^index/', dashboard_index),
    url(r'^infomanage/', infomanage_index),
    url(r'^database/', addPatient),
    url(r'^clinic/(.+)/$', clinic_index),
    url(r'^pharmacy/$', pharmacy_index),
    #url(r'^upload/$', upload_file),
    #url(r'^saved/', 'SaveProfile', name = 'saved'),
    url(r'^$', dashboard_index),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
