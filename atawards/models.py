from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,related_name = "profile",on_delete=models.CASCADE,)
    profile_photo = CloudinaryField('image')
    bio = models.CharField(max_length=500, blank=True, null=True)
    contact = models.CharField(max_length=50, blank=True, null=True)


    
    def __str__(self):
        return f'{self.user.username} Profile'
        
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()
    
    @classmethod
    def search_user(cls,name):
        return User.objects.filter(username__icontains = name)

class Project(models.Model):
    image = CloudinaryField('image')
    link = models.URLField(max_length=255, null=True)
    name = models.CharField(max_length=250, blank=True)
    description = models.TextField(max_length=250, blank=True)
    date = models.DateTimeField(auto_now_add=True, null=True)
    category = models.CharField(max_length=20)
    location = models.CharField(max_length=20)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="projects",null=True)


    def save_project(self):
        self.save()

    def delete_project(self):
        self.delete()

   
  # search project using project name
    @classmethod
    def search_project_name(cls, search_term):
        images = cls.objects.filter(
        name__icontains=search_term)
        return images  

    def str(self):
        return self.user.username


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    design_review = models.IntegerField(default=0, blank=True, null=True)
    usability_review = models.IntegerField(default=0, blank=True, null=True)
    content_review = models.IntegerField(default=0, blank=True, null=True)
    avg_review = models.IntegerField(default=0, blank=True, null=True)


    def save_review(self):
        self.save()

    def delete_review(self):
        self.delete()

    def __str__(self):
        return self.user.username
