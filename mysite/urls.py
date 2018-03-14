from django.urls import include, path
from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('passreset/',auth_views.password_reset,name='forgot_password1'),
    path('polls/', include('poll.urls')),
    path('admin/', admin.site.urls),
]