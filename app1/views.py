from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Task
from . forms import TaskForm

# Create your views here.

def index(request):
    tasks = Task.objects.all()
    if request.method == 'Post':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = TaskForm()

    context = {'tasks':tasks,'form':form}

    return render(request, 'list.html', context)


# def updateTask(request, pk):
    # task = Task.objects.get(id=pk)
    # if request.method =='POST':
    #     form = TaskForm(request.POST, instance=task)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('/')
    #     else:
    #         form = TaskForm(instance=task)
        
    # context = {'form':form}
    # return render (request, 'update.html', context)
def updateTask(request, pk):
	task = Task.objects.get(id=pk)

	form = TaskForm(instance=task)

	if request.method == 'POST':
		form = TaskForm(request.POST, instance=task)
		if form.is_valid():
			form.save()
			return redirect('/')
   

	context = {'form':form}

	return render(request, 'update.html', context)

def deleteTask(request, pk):
	item = Task.objects.get(id=pk)

	if request.method == 'POST':
		item.delete()
		return redirect('/')

	context = {'item':item}
	return render(request, 'delete.html', context)