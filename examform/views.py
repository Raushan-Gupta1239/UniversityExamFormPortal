from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import ExamForm

def index(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, "examform/login.html", {'error': 'Invalid credentials'})
    
    return render(request, "examform/login.html")

@login_required(login_url='index')
def dashboard(request):
    return render(request, "examform/dashboard.html")

def logout_view(request):
    logout(request)
    return redirect('index') 

def exam_form(request):
    if request.method == "POST":
        name = request.POST.get('Name')
        course = request.POST.get('Course')
        exam_date = request.POST.get('date')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        
        # Save data to database
        exam_data = ExamForm(
            name=name,
            course=course,
            exam_date=exam_date,
            address=address,
            phone=phone
        )
        exam_data.save()
        
        return render(request, "examform/exam-form.html", {'success': 'Exam form submitted successfully!'})
    
    return render(request, "examform/exam-form.html")  
      