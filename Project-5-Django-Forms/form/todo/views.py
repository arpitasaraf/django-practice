from django.shortcuts import render
from todo.forms import TodoForm
# Create your views here.

def createTodo_view(request):
    if(request.method == "POST"):
        title = request.POST.get("title")
        content = request.POST.get("content")
        
    fm = TodoForm()
    dict = {"form":fm , "pageName" : "Create Todo"}
    return render(request,"todo/todoForm.html",context=dict)