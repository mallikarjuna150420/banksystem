"""bankingsystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from customers import views as customer_view
from accounts import views as account_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', customer_view.customers, name='customer'),
    path('<uuid:pk>/', account_view.account_details, name='account_details'),
    path('account/<uuid:pk>/', account_view.transfer, name='transfer'),
    path('account/<uuid:id>/<uuid:rid>/', account_view.send, name='send'),
]
