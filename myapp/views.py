from django.shortcuts import render

# Create your views here.
def index(request):
    context = {"mensaje": "bienvenido a mi app en Django"}
    return render(request, 'myapp/index.html',context)
