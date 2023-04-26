from django.shortcuts import render

# Create your views here.
from app.forms import *
from django.http import HttpResponse

def insert_topic(request):
    tfo=TopicForm()
    d={'tfo':tfo}
    if request.method=="POST":
        td=TopicForm(request.POST)
        if td.is_valid():
            td.save()
            return HttpResponse('data is inserted sucessfully')
        else:
            return HttpResponse('data is not valid')

    return render(request,'insert_topic.html',d)
