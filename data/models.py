
from django.db import models
from django import forms
from django.contrib.auth.models import AbstractUser


class UserEmployee(AbstractUser):   

    pereant = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    mobile_number = models.CharField(max_length=10)
    code = models.CharField(max_length=24)
    
    def __str__(self):
        return f"{self.username}: {self.first_name}: {self.last_name}: {self.mobile_number}: {self.email}"


class Applicant(models.Model):

    STATUS_CHOICES = [
        (1, 'Activate'),
        (2, 'Close'),
        (3, 'Assign'),
        (4, 'New'),
    ]

    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    agent = models.ForeignKey(UserEmployee,on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=24)
    mobile = models.BigIntegerField()
    email = models.EmailField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    address = models.CharField(max_length=255)
    status = models.CharField(max_length=24, choices=STATUS_CHOICES)
    github = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)

    def __str__(self):
        return f"{self.fresher_expiriance}: {self.agent_socialmedia}: {self.name}"


class Education(models.Model):

    candidate = models.ForeignKey(Applicant, on_delete=models.CASCADE, related_name="education")
    title = models.CharField(max_length=255)
    degree_name = models.CharField(max_length=24)
    collage_name = models.CharField(null=True, max_length=24)
    percentage = models.FloatField(null=True)
    passing_year = models.DateField()

    #linkein_link = models.CharField(max_length=24, blank=True)
    #github_link = models.CharField(max_length=24, blank=True)
    #website_link = models.CharField(max_length=24, blank=True)  

    def __str__(self):
        return f"{self.degree_name}: {self.collage_name}: {self.percentage}: {self.title}: {self.name} "


class Experience(models.Model):

    candidate = models.ForeignKey(Applicant, on_delete=models.CASCADE, related_name="experiance")
    company_name = models.CharField(max_length=24)
    year_of_experience = models.IntegerField() 
    work = models.TextField()
    domain = models.CharField(max_length=24)
    salary = models.FloatField(null=True)

    def __str__(self):
        return f"{self.company_name}: {self.year_of_experience}: {self.work}: {self.domain}: {self.salary}: {self.name}"

  
class Skills(models.Model):

    candidate = models.ForeignKey(Applicant, on_delete=models.CASCADE)
    skill_detail = models.TextField()


class Academics(models.Model):

    candidate = models.ForeignKey(Applicant, on_delete=models.CASCADE)
    academic_detail = models.TextField()


class AreaOfInterest(models.Model):

    candidate = models.ForeignKey(Applicant, on_delete=models.CASCADE)
    area_of_interest_detail = models.TextField()


class Language(models.Model):

    candidate = models.ForeignKey(Applicant, on_delete=models.CASCADE)
    language = models.CharField(max_length=20,blank=False)
    order = models.IntegerField(default=1)
    SCALE_CHOICES= (
        (5, 'Native'),
        (4, 'Full professional proficiency'),
        (3, 'Professional working proficiency'),
        (2, 'Limited professional proficiency'),
        (1, 'Elementary professional proficiency')
        )
    level = models.IntegerField(help_text='Choice between 1 and 5', default=5, choices=SCALE_CHOICES)
