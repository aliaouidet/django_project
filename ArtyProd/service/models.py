from django.db import models
from django.db.models.constraints import UniqueConstraint
from django.contrib.auth.models import AbstractUser, Group, Permission
#to create migration files
#python manage.py makemigrations

#to migrate migration files
#python manage.py migrate




class User(AbstractUser):
    username = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='user_photos', null=True, blank=True)
    email = models.EmailField()
    phone = models.CharField(max_length=15)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_groups',
        related_query_name='custom_user'
    )

    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_permissions',
        related_query_name='custom_user'
    )

    def __str__(self):
        return f"{self.last_name}, {self.first_name}"
class Project(models.Model):
    STATUS_CHOICES = (
        ('IP', 'In Progress'),
        ('C', 'Completed'),
    )
    
    title = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    services = models.ManyToManyField('Service', through='ProjectService')
    assigned_team = models.ForeignKey('Team', on_delete=models.SET_NULL, null=True)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default='IP')
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.title}"
    

class Service(models.Model):
    SERVICE_TYPES = (
        ('GC', 'Graphic charter'),
        ('3D', '3D object'),
        ('SC', 'Scripting'),
    )
    name = models.CharField(max_length=50)
    icon = models.ImageField(upload_to='service_icons', blank=True, null=True)
    service_type = models.CharField(max_length=2, choices=SERVICE_TYPES)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):      
        return f"{self.name}"
    

class ProjectService(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.project.title} - {self.service.name}"
    

class Team(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    members = models.ManyToManyField(User, through='TeamMember')
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.name}"

class TeamMember(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    member = models.ForeignKey(User, on_delete=models.CASCADE)
    is_leader = models.BooleanField(default=False)
    linkedin = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['team'], condition=models.Q(is_leader=True),
                name='unique_team_leader'
            )
        ]

    def __str__(self):
        return f"{self.member.first_name} {self.member.last_name}"


class ProjectFile(models.Model):
    PROJECT_FILE_TYPES = (
        ('IMG', 'Image'),
        ('VID', 'Video'),
        ('PDF', 'PDF Document'),
    )
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=3, choices=PROJECT_FILE_TYPES)
    file = models.FileField(upload_to='project_files')
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.project.title} - {self.file_type}"


    class Meta:
        constraints = [
            UniqueConstraint(fields=['project', 'file_type'], name='unique_project_file')
        ]
class Testimonial(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    author_name = models.CharField(max_length=100)
    author_company = models.CharField(max_length=100)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.project.title} - {self.author_name}"

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"{self.title}"
    
class Comment(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.project.title} - {self.user.first_name} {self.user.last_name},"