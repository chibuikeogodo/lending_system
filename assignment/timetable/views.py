from django.shortcuts import render, redirect, HttpResponse
from .forms import ExamForm
from .models import TimeTable

# Create your views here.

def home(request):
    url = 'home.html'
    return render(request, url)

def ExamSetup(request):
    url = 'exam_setup.html'
    form = ExamForm()
    if request.method == 'POST':
        form = ExamForm(request.POST)
        if form.is_valid:
            form.save()
        return  redirect('timetable:examsetup')
    return render(request, url, {'form':form})

def ExamTime(request):
    url = 'exam_time.html'
    exam = TimeTable.objects.all()
    return render(request, url, {'exams': exam})

def TimeDelete(request, id):
    exam = TimeTable.objects.get(id=int(id))
    exam.delete()
    return redirect('timetable:examtime')

def admin(request):
    url = 'admin_page.html'
    return render(request, url)
