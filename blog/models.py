from django.db import models
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField
from multiselectfield import MultiSelectField




LANGUAGES = [('English','English'),('Germany','Germany'),('French','French')]
# As a sample I choose limit option of skills.
SKILLS = [
          ('Python', 'Python'),('Django', 'Django'),('Html/Css', 'Html/Css'),
          ('Git','Git'),('Javascripts', 'Javascripts'),('Java', 'Javas'),
          ('C', 'C'),('Php', 'Php'),('Laravel', 'Laravel'),
          ]



class Personal_info(models.Model):
    resumetitle = models.CharField('Resume Title ',max_length=200)
    biography = models.TextField(blank = True)
    name = models.CharField('Name',max_length=200, blank = True)
    email = models.EmailField('Email',blank=True)
    city= models.CharField('City ',max_length = 100 , blank = True)
    birth_date= models.DateField(default = "1990-06-21")
    address = models.CharField('Address ',max_length=500)
    skills = MultiSelectField(choices=SKILLS)
    languages = MultiSelectField(choices=LANGUAGES)
    created_date = models.DateTimeField('Created Date ',default = timezone.now)
    mobilephone = PhoneNumberField()
    def formatted_phone(self):
        for i in range(14):
            a = str(0)+str(self.mobilephone)[3:6]
            b = str(self.mobilephone)[6:]
        return f'{a}-{b}'

    degrees= models.CharField('Degrees ',max_length = 100, blank = True)
    university=models.CharField('University ',max_length = 200, blank = True)
    major=models.CharField('Major ',max_length = 100, blank = True)
    graduation=models.CharField('Graduation ',max_length = 100, blank = True)

