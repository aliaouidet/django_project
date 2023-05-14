from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, Project, Service, ProjectService, Team, TeamMember, ProjectFile, Testimonial, Article, Comment
from django.contrib.auth.models import Group
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import User

class CustomUserAdmin(UserAdmin):
    list_display = ('email', 'first_name', 'last_name', 'photo', 'phone', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'photo', 'phone')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email', 'first_name', 'last_name', 'photo', 'phone',
                'password1', 'password2', 'is_staff', 'is_active', 'groups', 'user_permissions',
            ),
        }),
    )
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)

admin.site.register(User, CustomUserAdmin)
class UserAdmin(BaseUserAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email', 'phone')
    search_fields = ('first_name', 'last_name', 'email', 'phone')
    ordering = ('id',)
    # Define fieldsets to include additional fields
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'phone', 'photo')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'first_name', 'last_name', 'photo', 'email', 'phone', 'password1', 'password2'),
        }),
    )

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'client', 'start_date', 'end_date', 'status')
    search_fields = ('title', 'client__first_name', 'client__last_name')
    list_filter = ('status',)

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'service_type')
    search_fields = ('name',)

class ProjectServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'project', 'service')
    search_fields = ('project__title', 'service__name')

class TeamAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name', 'leader__first_name')

class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('id', 'team', 'member', 'is_leader')
    search_fields = ('team__name', 'member__first_name', 'member__last_name')

class ProjectFileAdmin(admin.ModelAdmin):
    list_display = ('id', 'project', 'file_type', 'file')
    search_fields = ('project__title',)
    list_filter = ('file_type',)

class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('id', 'project', 'author_name', 'author_company')
    search_fields = ('project__title', 'author_name', 'author_company')

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'created_at', 'updated_at')
    search_fields = ('title', 'content', 'author__first_name', 'author__last_name')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'project', 'user', 'text')
    search_fields = ('project__title', 'user__first_name', 'user__last_name', 'text')

# Register models with custom admin classes

admin.site.register(Project, ProjectAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(ProjectService, ProjectServiceAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(TeamMember, TeamMemberAdmin)
admin.site.register(ProjectFile, ProjectFileAdmin)
admin.site.register(Testimonial, TestimonialAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment, CommentAdmin)
# Unregister the Group model from admin since we are using a custom User model
admin.site.unregister(Group)