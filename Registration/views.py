from django.shortcuts import render
from Registration.models import Course
from Registration.models import Mentor
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.

def index(request):
    return render (request , "index.html")

def course(request):
    if request.method == 'POST':
        c_code =request.POST['code']
        c_desc =request.POST['desc']
        data=Course(code=c_code,description=c_desc)
        data.save()
        allcourse = Course.objects.all().values()
        dict = {
            'message':'Successful, Data Save',
            'allcourse': allcourse,
        }
    else :
        allcourse = Course.objects.all().values() 
        dict ={
            'message':'Unsuccessful',
            'allcourse': allcourse,
        }
        
    return render (request,"course.html",dict)

def mentor(request):
    if request.method == 'POST':
        m_id =request.POST['MID']
        m_name =request.POST['MNAME']
        m_email =request.POST['MEMAIL']
        data=Mentor(mentorCd=m_id,mentorName=m_name,mentorEmail=m_email)
        data.save()
        allmentor = Mentor.objects.all().values()
        dict = {
            'message':'Successful, Data Save',
            'allmentor': allmentor,
        }
    else : 
        allmentor = Mentor.objects.all().values()
        dict ={
            'message':'Unsuccessful',
            'allmentor': allmentor,
        }
        
    return render (request,"mentor.html",dict)

def search(request):
    if request.method == 'GET':
        c_code = request.GET.get('c_code')

        if c_code:
            data = Course.objects.filter(code=c_code.upper())
        else:
            data = None

        context = {
            'data': data
        }

        return render(request, "search.html", context)

    return render(request, "search.html")

def search_mentor(request):
    if request.method == "GET":
        mentorCd = request.GET.get('mentorCd')

        if mentorCd:
            data = Mentor.objects.filter(mentorCd=mentorCd.upper())
        else:
            data =  None
        

        context = {
            'data': data
        }

        return render(request,"search_mentor.html", context)

    
    return render(request,"search_mentor.html")

def update_course(request,code):
    data=Course.objects.get(code=code)
    dict = {
        'data':data 
    }
    return render (request , "update_course.html", dict)

def save_update_course(request,code):
    c_desc= request.POST['description']
    data=Course.objects.get(code=code)
    data.description = c_desc
    data.save()
    return HttpResponseRedirect(reverse("course"))

def delete_course(request,code):
    data = Course.objects.get(code=code)
    data.delete()
    return HttpResponseRedirect(reverse('course'))