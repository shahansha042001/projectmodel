from django.shortcuts import render

# Create your views here.
from app.forms import *
from django.http import HttpResponse


def insert_topic(request):
    ETFO=TopicForm()
    d={'ETFO':ETFO}

    if request.method=='POST':
        TFDO=TopicForm(request.POST)
        if TFDO.is_valid():
            TFDO.save()
            return HttpResponse('insert_topic is done Successfully')
    return render(request,'insert_topic.html',d)



def insert_Webpage(request):
    EWFO=WebpageForm()
    d={'EWFO':EWFO}

    if request.method=='POST':
        WFDO=WebpageForm(request.POST)
        if WFDO.is_valid():
            WFDO.save()
            return HttpResponse('insert_Webpage is done Successfully')
    return render(request,'insert_Webpage.html',d)



def insert_AccessRecord(request):
    EAFO=AccessRecordForm()
    d={'EAFO':EAFO}

    if request.method=='POST':
        AFDO=AccessRecordForm(request.POST)
        if AFDO.is_valid():
            AFDO.save()
            return HttpResponse('insert_AccessRecord is the done successfully')
    return render(request,'AccessRecord.html',d)