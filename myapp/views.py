from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import Task
# Create your views here.
# def index(request):
#     task = Task.objects.all()
#     return render(request,'myapp/index.html', {'task':task})

# def add_form(request):
#     if request.method =="POST":
#         name = request.POST.get("name","")
#         priority =  request.POST.get("priority","")
#         task = Task(name=name, priority=priority)
#         task.save()
#         return redirect('/')
#     return render(request,'myapp/add.html')


def delete(request,id):
    task = Task.objects.get(id=id)
    if request.method == "POST":
        task.delete()
        return redirect('/')

    return render(request,'myapp/delete.html')

def index_form(request):
    if request.method =="POST":
        name = request.POST.get("name","")
        priority =  request.POST.get("priority","")
        task = Task(name=name, priority=priority)
        task.save()
        return redirect('/')

    else:
        task = Task.objects.all()
        return render(request,'myapp/index.html', {'task':task})

        
    