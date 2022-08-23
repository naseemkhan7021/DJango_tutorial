from django.urls import reverse
from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render

# GLOBAL var, access by all visitor
# tasks = ["Eat", "Sleep", "Cod", "Repeat"]
# tasks = []

# form to add New tasks
class NewTaskForm(forms.Form):
    task = forms.CharField(label='Name', max_length=10)

# Create your views here.
def index(request):
    if "tasks" not in request.session:
        request.session["tasks"] = []
    return render(request, 'tasks/index.html', {
        "tasks": request.session["tasks"],
        "pageTitle": 'Task List'
    })


def add(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if(form.is_valid()):
            task = form.cleaned_data["task"]
            # tasks.append(task) # this is for GLOBLE VARIABLE
            request.session["tasks"] += [task]
            return HttpResponseRedirect(reverse("tasks:index"))
        else:
            return render(request, 'tasks/add.html', {
                "form": form
            })
    return render(request, 'tasks/add.html', {
        "pageTitle": 'Add Task',
        "form": NewTaskForm()
    })
