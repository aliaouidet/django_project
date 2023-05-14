from django.shortcuts import render, redirect
from .models import Project, Service, Team, TeamMember, Testimonial, Article
from django.contrib.auth.forms import UserCreationForm

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

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
