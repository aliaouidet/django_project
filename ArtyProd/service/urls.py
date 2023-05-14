from django.urls import path
from .views import homePageView, servicesPageView,register
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
app_name = 'servive'

urlpatterns = [
    
    path('', homePageView, name='home'),
    path('services/', servicesPageView, name='services'),
    path('register/', register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),


]+ static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)   