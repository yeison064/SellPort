from django.db import models
from PIL import Image
# Create your models here.


class PersonalInformation(models.Model):
    name = models.CharField(max_length=250,blank=False)
    photo = models.ImageField(upload_to='profile_photo',blank=False)
    tagline = models.CharField(max_length=500,blank=False)
    email = models.EmailField(max_length=500,blank=False)
    phone = models.CharField(max_length=15,blank=True)
    location = models.CharField(max_length=200,blank=False)
    locationURL = models.URLField(max_length=300,blank=True)
    twtrLink = models.URLField(max_length=300,blank=True)
    gthbLink = models.URLField(max_length=300,blank=True)
    linkedLink = models.URLField(max_length=300,blank=True)
    instaLink = models.URLField(max_length=300,blank=True)
    mediumLink = models.URLField(max_length=300,blank=True)

    class Meta:
        verbose_name = 'Personal Information'
        verbose_name_plural = 'Personal Information'

class AboutMe(models.Model):
    text = models.TextField("About me")
    resumeLink = models.URLField(max_length=1000,blank=False)
    class Meta:
        verbose_name = 'About Me'
        verbose_name_plural = 'About Me'

class mySkills(models.Model):
    skill = models.CharField(max_length=100,blank=False)

    class Meta:
        verbose_name = 'My Skills'
        verbose_name_plural = 'My Skills'
    def __str__(self):
        return self.skill

class whatIDo(models.Model):
    heading = models.CharField(max_length=100,blank=False)
    text = models.TextField()

    class Meta:
        verbose_name = 'What I Do'
        verbose_name_plural = 'What I Do'

class TechSkills(models.Model):
    skill = models.CharField(max_length=100,blank=False)
    percentage = models.IntegerField()
    class Meta:
        verbose_name = 'Technical Skills'
        verbose_name_plural = 'Technical Skills'
    
    def __str__(self):
        return self.skill+' - '+str(self.percentage)+'%'

class ProfSkills(models.Model):
    skill = models.CharField(max_length=100,blank=False)
    percentage = models.IntegerField()
    class Meta:
        verbose_name = 'Professional Skills'
        verbose_name_plural = 'Professional Skills'
    
    def __str__(self):
        return self.skill+' - '+str(self.percentage)+'%'

class educationalEx(models.Model):
    name = models.CharField(max_length=100,blank=False)
    org = models.CharField(max_length=150,blank=False)
    time = models.CharField(max_length=50,blank=False)
    text = models.TextField()

    class Meta:
        verbose_name_plural = 'Educational Experience'
        verbose_name = 'Educational Experience'

class profEx(models.Model):
    role = models.CharField(max_length=100,blank=False)
    org = models.CharField(max_length=150,blank=False)
    orgLink = models.URLField(max_length=300,blank=False)
    time = models.CharField(max_length=30,blank=False)
    work = models.TextField()
    
    class Meta:
        verbose_name = 'Professtional Experience'
        verbose_name_plural = 'Professtional Experience'

class featuredPost(models.Model):
    image = models.ImageField(upload_to='featuredPost',blank=False)
    heading = models.CharField(max_length=200)
    postMetaDetail = models.CharField(max_length=100)
    postDetail = models.CharField(max_length=300)
    link = models.URLField(max_length=500,blank=False)

    class Meta:
        verbose_name_plural = 'Featured Post'
        verbose_name = 'Featured Post'

class testimonials(models.Model):
    image = models.ImageField(upload_to='testimonial_photos')
    name = models.CharField(max_length=100,blank=False)
    role = models.CharField(max_length=100)
    text = models.TextField()

    class Meta:
        verbose_name = 'Testimonial'
        verbose_name_plural = 'Testimonial'

class contact(models.Model):
    fname = models.CharField(max_length=200)
    lname = models.CharField(max_length=200)
    email = models.EmailField(max_length=300)
    message = models.TextField()
    def __str__(self):
        return 'Message from '+self.fname
    class Meta:
        verbose_name = 'Messages'
        verbose_name_plural = 'Messages'