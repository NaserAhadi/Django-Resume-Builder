from django import forms
from . models import Personal_info
from easy_select2 import select2_modelform
from django_select2.forms import Select2MultipleWidget


YEARS= [x for x in range(1970,2021)]
# As a sample I choose limit option of Cities.
CITIES = [('Tehran', 'Tehran'),('Karaj', 'Karaj')]
DEGREES = [('Bachelor','Bachelor'),('MA','MA'),('Doctorate','Doctorate')]



class Personal_info_Form(forms.ModelForm):
    birth_date= forms.DateField(
                label='What is your birth date?',
                 initial="1990-07-21",
                 widget=forms.SelectDateWidget(years=YEARS)
                 )

    city =forms.CharField(label='Choose your city  ', widget=forms.Select(choices=CITIES))



    major =forms.CharField(label='Major',widget=forms.TextInput(
                                                    attrs={
                                                             'class':'form-control',
                                                             'placeholder':'Civil Engineer'
                                                            }
                                                        ))


    address =forms.CharField(label='Address',widget=forms.TextInput(
                                                    attrs={
                                                             'class':'form-control',
                                                             'placeholder':'Malard - East Danesh st'
                                                            }
                                                        ))
    resumetitle =forms.CharField(label='Resume Title',widget=forms.TextInput(
                                                    attrs={
                                                             'class':'form-control',
                                                             'placeholder':'Python/Django Developer '
                                                            }
                                                        ))
    name =forms.CharField(label='Name',widget=forms.TextInput(
                                                    attrs={
                                                             'class':'form-control',
                                                             'placeholder':'Naser Ahadi'
                                                            }
                                                        ))
    email =forms.CharField(label='Email',widget=forms.EmailInput(
                                                  attrs={
                                                            'class':'form-control',
                                                           'placeholder':'email@example.com'
                                                           }
                                                       ))

    mobilephone =forms.CharField(label='Mobile Phone',widget=forms.TextInput(
                                                    attrs={
                                                          'class':'form-control',
                                                              'placeholder':'+98912XXXXXXX'
                                                            }
                                                        ))


    graduation =forms.DateField(label='Date of Graduation',widget=forms.SelectDateWidget(years=YEARS))


    biography =forms.CharField(label='Biography',widget=forms.Textarea(
                                                     attrs={
                                                              'class':'form-control',
                                                              'placeholder':'Write something about yourself'
                                                             }
                                                         ))


    degrees =forms.CharField(label='Choose your last degrees  ', widget=forms.Select(choices=DEGREES))

    university =forms.CharField(
                                label='University Name' ,
                                widget=forms.TextInput(
                                                    attrs={
                                                             'class':'form-control',
                                                             'placeholder':'K.N.Toosi University of Technology '
                                                            }
                                                        )
                                )


    class Meta:
        model = Personal_info
        fields = [
        'resumetitle','name','birth_date','mobilephone','email',
        'city','address','skills','languages','degrees','university',
        'major','graduation','biography',
        ]
