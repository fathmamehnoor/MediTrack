"""
URL configuration for hospital_management project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from hospital import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('a',views.addsp),
    path('dreg',views.doctor_reg),
    path('preg',views.patient_reg),
    path('pview',views.patientview),
    path('bview/', views.bookview),
    path('adminhome',views.adminhome),
    path('',views.home),
    path('approvest/<int:uid>',views.approvest),
    path('bview/approveb/<int:bid>/', views.approveb),
    path('lg',views.logins),
    path('dhome',views.doctorhome),
    path('phome',views.patienthome),
    path('lgout',views.lgout),
    path('dview', views.doctorview),
    path('updateprofile',views.updateprofile),
    path('doctorupdate',views.doctorupdate),
    path('pbook',views.pbook,  name='pbook'),
    path('update_patient/<int:uid>',views.update_patient),
    path('update_doctor/<int:uid>',views.update_doctor),
]
