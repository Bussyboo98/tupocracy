
from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from django.shortcuts import reverse
from django.utils import timezone

from django.contrib.auth.models import User

import datetime




class HomePageBanner(models.Model):
    banner_title = models.TextField()
    banner_img =   models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.banner_title

    class Meta():
        verbose_name_plural = 'Home Page Banner'

    def get_banner(self):
        if self.banner_img:
            return self.banner_img.url



class AboutUsModel(models.Model):
    name = models.CharField(max_length=20)
    abt_img = models.ImageField(blank=True, null=True)
    about_content = HTMLField('About Content')
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta():
        verbose_name_plural = 'About Us'
    
    def get_abt_img(self):
        if self.abt_img:
            return self.abt_img.url
        else:
            return '/static/webapp/assets/images/coder3.jpg'

  

class CreditModel(models.Model):
    name = models.CharField(max_length=20)
    img = models.ImageField(blank=True, null=True)
    content = HTMLField('Content', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta():
        verbose_name_plural = 'Credit'
    
    def get_img(self):
        if self.get_img:
            return self.img.url

class Award(models.Model):
    name = models.CharField(max_length=20)
    img = models.ImageField(blank=True, null=True)
    content = HTMLField('Content', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta():
        verbose_name_plural = 'Award'
    
    def get_img(self):
        if self.get_img:
            return self.img.url

class Emytology(models.Model):
    name = models.CharField(max_length=100) 
    content = HTMLField('Content', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta():
        verbose_name_plural = 'Emytology'

class Community(models.Model):
    title = models.CharField(max_length=200) 
    name = models.CharField(max_length=100) 
    img = models.ImageField(blank=True, null=True)
    content = HTMLField('Content', blank=True, null=True)
    link = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
     
    def get_img(self):
        if self.get_img :
            return self.img.url
        else:
            return '../static/public/img/emy.jpg'
    class Meta():
        verbose_name_plural = 'Community'


class CommunityArticle(models.Model):
    title = models.CharField(max_length=500) 
    name = models.CharField(max_length=200, verbose_name="Author", blank=True) 
    slug = models.SlugField(unique=True)
    img = models.ImageField(blank=True, null=True)
    content = HTMLField('Content', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
     
    def get_img(self):
        if self.get_img :
            return self.img.url
        else:
            return '../static/public/img/emy.jpg'
    class Meta():
        verbose_name_plural = 'Community Article'
    
    def get_post_url(self):
        return reverse('tupo_app:single_comm', kwargs={
            'slug': self.slug,
        })
    

class Nomination(models.Model):
    ONE = "Dr."
    TWO = "Doctor"
    THREE = "Mr."
    FOUR = "Mrs."   
    FIVE = "Ms."   
    CHOOSE = ""

    TITLE= [
         (ONE, 'Dr.'),
         (TWO, ' Doctor'),
         (THREE, 'Mr.'),
         (FOUR, 'Mrs.'),
         (FIVE, 'Ms.'  ),
         (CHOOSE, 'Choose Title')
    ]

    ONE = "Yes"
    TWO = "No"
  
    CHOOSE = ""

    TUPO= [
         (ONE, 'Yes'),
         (TWO, ' No'),
         
         (CHOOSE, 'Select')
    ]
    award_title = models.CharField(max_length=100,)
    title = models.CharField(max_length=40, choices=TITLE, default=CHOOSE)
    da_ti= models.CharField(max_length=200, verbose_name="Date/Time")
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    position =models.CharField(max_length=100)
    birthday = models.CharField(max_length=200, verbose_name="Birthday")
    employer = models.CharField(max_length=100)
    phone = models.CharField(max_length=50, verbose_name='Phone')
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    home = models.CharField(max_length=200, verbose_name="Home Address")
    email = models.CharField(max_length=40,)
    select_all = models.CharField(max_length=40, choices=TUPO, default=CHOOSE)
    member = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name

    class Meta():
        verbose_name_plural = 'Nomination'


class Principal(models.Model):
    ONE = "Dr."
    TWO = "Doctor"
    THREE = "Mr."
    FOUR = "Mrs."   
    FIVE = "Ms."   
    CHOOSE = ""

    TITLE= [
         (ONE, 'Dr.'),
         (TWO, ' Doctor'),
         (THREE, 'Mr.'),
         (FOUR, 'Mrs.'),
         (FIVE, 'Ms.'  ),
         (CHOOSE, 'Choose Title')
    ]

    ONE = "Yes"
    TWO = "No"
  
    CHOOSE = ""

    TUPO= [
         (ONE, 'Yes'),
         (TWO, ' No'),
         
         (CHOOSE, 'Select')
    ]
  
    title = models.CharField(max_length=40, choices=TITLE, default=CHOOSE)
  
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    position =models.CharField(max_length=100)
 
    employer = models.CharField(max_length=100)
    phone = models.CharField(max_length=50, verbose_name='Phone')
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    home = models.CharField(max_length=200, verbose_name="Home Address")
    email = models.CharField(max_length=40,)
    select_all = models.CharField(max_length=40, choices=TUPO, default=CHOOSE)
    member = models.TextField()
    name1 = models.CharField(max_length=100)
    affilation1 = models.CharField(max_length=100)
    name2 = models.CharField(max_length=100)
    affilation2 = models.CharField(max_length=100)
    name3 = models.CharField(max_length=100)
    affilation3 = models.CharField(max_length=100)
    name4 = models.CharField(max_length=100)
    affilation4 = models.CharField(max_length=100)
    name5 = models.CharField(max_length=100)
    affilation5 = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name

    class Meta():
        verbose_name_plural = 'Principal Nominator'
   
        

    
   