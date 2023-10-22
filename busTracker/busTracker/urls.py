from django.contrib import admin
from django.urls import path, include
from cuentas import views as views_cuentas

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register', views_cuentas.signupaccount),
    path('accounts/', include('cuentas.urls')),
    path('bus/', include('bus.urls')),
    path('', include('chatbot.urls')),

]
