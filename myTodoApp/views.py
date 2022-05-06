from django.shortcuts import render, redirect
from .models import Category, TodoData

#Using a function based view
def index(request): 
    categories = Category.objects.all()
    PendingTask = TodoData.objects.all()
    if request.method == "POST": 
        if "Addtask" in request.POST:
            name_of_task = request.POST["name_of_task"] 
            deadline = str(request.POST["deadline"]) 
            category = request.POST["category_select"] 
            content = name_of_task + " -- " + deadline + " " + category 
            Todo = TodoData(name_of_task=name_of_task, task=content, due_date=deadline, category=Category.objects.get(type=category))
            Todo.save() 
            return redirect("/")
        if "Deletetask" in request.POST: 
            checkedlist = request.POST["checkedbox"] 
            for todo_id in checkedlist:
                todo = TodoData.objects.get(id=int(todo_id)) 
                todo.delete()
    return render(request, "index.html", {"PendingTask": PendingTask, "categories":categories})