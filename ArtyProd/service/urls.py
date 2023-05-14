
from django.urls import path

from .views import homePageView, login_view, servicesPageView,registrationPageView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    
    path('', homePageView, name='home'),
    path('services/', servicesPageView, name='services'),
    path('register/', registrationPageView, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),


]+ static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)   