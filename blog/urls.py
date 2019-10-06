from django.urls import path,include
from .  import views


urlpatterns = [
    path('', views.create , name = 'create_resume'),
    path('resume', views.printing , name = 'resume'),
    path('resume/pdf/' , views.print2pdf , name = 'print2pdf'),
]
