from django.shortcuts import render,redirect
from . models import Personal_info
from . forms import Personal_info_Form
from django.utils import timezone
from .render import render_to_pdf


def printing(request):
    info = Personal_info.objects.last()
    return render(request,'blog/resume.html' , {'info':info})


def create(request):
    if request.method == 'POST':
        form = Personal_info_Form(request.POST)
        if form.is_valid():
            info = form.save(commit = False)
            info.save()
            return redirect('resume')
    else:
        form = Personal_info_Form()
    return render(request,'blog/create_resume.html' , {'form':form})


def print2pdf(request):
    info = Personal_info.objects.last()

    return render_to_pdf(
            'blog/print_resume.html',
            {
                'pagesize':'A4',
                'info':info,
            }
        )
