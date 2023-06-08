from ckeditor_uploader import fields
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Technology(models.Model):
    class Meta:
        verbose_name = 'Technology'
        verbose_name_plural = 'Technologies'
    technology_name = models.CharField(max_length=100, null=False, blank=False)
    technology_uil_name = models.CharField(max_length=100, null=False, blank=False, default='brackets-curly')

    def __str__(self):
        return f'{self.technology_name}'


class Project(models.Model):
    project_name = models.CharField(max_length=255, blank=False, null=False)
    description = models.TextField(null=False, blank=False)
    technologies = models.ManyToManyField(Technology, related_name='technology')
    project_image = models.ImageField(upload_to='projects')
    project_url = models.URLField(blank=False, null=True)
    project_github_url = models.URLField(blank=False, null=True, default="https://github.com")


    def __str__(self):
        return f'{self.project_name}, {self.project_url}'


    
class UserProfile(models.Model):
    class Meta:
        verbose_name = 'User Profile'
        verbose_name_plural = 'User Profiles'

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(blank=True, null=True, upload_to="avatar")
    title = models.CharField(max_length=200, blank=True, null=True)
    bio = fields.RichTextUploadingField(blank=True, null=True)
    cv = models.FileField(blank=True, null=True, upload_to="cv")
    linkedin = models.URLField(default='https://linkedin.com')
    twitter = models.URLField(default='https://twitter.com')
    github = models.URLField(default='https://github.com')
    whatsapp = models.URLField(default='https://whatsapp.com')

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'


class Contact(models.Model):
    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'
        ordering = ['-timestamp']

    name = models.CharField(max_length=255, blank=False, null=False)
    email = models.EmailField(blank=False, null=False)
    message = models.TextField(blank=False, null=False)
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.name}, {self.email}'



class Blog(models.Model):
    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'
        ordering = ['-timestamp']

    title = models.CharField(max_length=255, blank=False, null=False)
    blog_image = models.ImageField(upload_to='blogs', default='blogs/default.jpg')
    content = fields.RichTextUploadingField(blank=False, null=False)
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='author')
    timestamp = models.DateField(default=timezone.now)
  

    def __str__(self):
        return f'{self.title}'

class SoftSkill(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    
    def __str__(self):
        return f'{self.name}'