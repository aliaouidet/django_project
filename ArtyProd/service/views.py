from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import UserRegistrationForm
from .models import Project, Service, Team, TeamMember, Testimonial, Article
from django.contrib.auth import views as auth_views
from .forms import EmailLoginForm


def login_view(request):
    if request.method == 'POST':
        form = EmailLoginForm(request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = EmailLoginForm(request)
    
    return render(request, 'login.html', {'form': form})
def registrationPageView(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user.set_password(password)
            user.backend = 'django.contrib.auth.backends.ModelBackend'  # Specify the authentication backend
            user.save()
            authenticated_user = authenticate(request, username=username, password=password)
            login(request, authenticated_user)
            return redirect('home')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration.html', {'form': form})

def homePageView(request):
    projects = Project.objects.all()
    return render(request, 'home.html', {'projects': projects})

def servicesPageView(request):
    services = Service.objects.all()
    return render(request, 'services.html', {'services': services})

def portfolio_view(request):
    projects = Project.objects.all()
    testimonials = Testimonial.objects.all()
    return render(request, 'portfolio.html', {'projects': projects, 'testimonials': testimonials})


def team_view(request):
    team_members = TeamMember.objects.all()
    return render(request, 'team.html', {'team_members': team_members})

def contact_view(request):
    if request.method == 'POST':
        # Handle contact form submission
        pass
    else:
        # Render contact form template
        return render(request, 'contact.html')

def blog_view(request):
    articles = Article.objects.all()
    return render(request, 'blog.html', {'articles': articles})
