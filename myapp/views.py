from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from myapp.models import *
from myapp import forms
import add_data
# Create your views here.

def page1(request):
    return HttpResponse("<h1>welcome to page 1</h1>")

def page2(request):
    return render(request,'page2.html',context={'data':"data is passed"})

def topic(request):
    d={'objects':Topic.objects.all()}
    return render(request,'page3.html',context=d)

def records(request):
    d={'objects':Access_Records.objects.order_by('date')}
    return render(request,'page4.html',context=d)

def page5(request):
    data=Topic.objects.all()
    return render(request,'page8.html',context={'objects':data})

def display(request):
    topics=Topic.objects.all()
    qs=Webpage.objects.none()
    for top in topics:       
        if top.topic in request.POST:
            data=request.POST.get(top.topic,"Key not found")
            qs=qs.union(Webpage.objects.all().include(topic=data))
    return render(request,'page6.html',context={'objects':qs})

def page7(request):
    data=Topic.objects.all()
    return render(request,'page7.html',context={'objects':data})


def delete(request):
    data=request.POST.get("topic","Key not found")
    Topic.objects.get(topic=data).delete()
    return HttpResponse("<h1>Deletion successfull</h1>")

def page9(request):
    return render(request,'page9.html')

def update(request):
    oname=request.POST.get('oname')
    nname=request.POST.get('nname')
    Webpage.objects.filter(url=oname).update(url=nname)
    return HttpResponse("Data is updated")

def page10(request):
    form=forms.ContactForm()
    if request.method=="POST":
        form=forms.ContactForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            return render(request,'page10.html',context={'form':forms.ContactForm()})

    return render(request,'page10.html',context={'form':form})


def report(request):
    if request.method=="POST":
        form_data=forms.ContactForm(request.POST)
        #form is valid or not
        if form_data.is_valid():
            return render(request,'page11.html',context=form_data.cleaned_data)
        else:
            return HttpResponse("iNVALID FROM")
    return HttpResponse("Form Submission Error")

def create_topic(request):
    if not request.POST:
        pass
    
    else:
        add_data.add_topic(request.POST.get('topic'))
        
    return render(request,'create_topic.html') 

def create_webpage(request):
    topic=Topic.objects.all()
    if not request.POST:
        pass
    
    else:
        
        add_data.add_webpage(request.POST.get('topic'),request.POST.get('webpage'),request.POST.get('url'))
        
    return render(request,'create_webpage.html',context={'objects':topic})


def Model_Form(request):
    form=forms.Access_Record_Form()
    if request.method=='POST':
        form_data=forms.Access_Record_Form(request.POST)
        if form_data.is_valid():
            form_data.save(commit=True)
    return render(request,'model_form_demo.html',context={'form':form})