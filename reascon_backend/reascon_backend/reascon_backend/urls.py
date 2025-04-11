"""
URL configuration for reascon_backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from contacts.views import ContactCreateView, ProjectInquiryCreateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/contact/', ContactCreateView.as_view(), name='contact-create'),
    path('api/project-inquiry/', ProjectInquiryCreateView.as_view(), name='project-inquiry-create'),
]