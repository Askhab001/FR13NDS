from django.shortcuts import render


def index(request):
    return render(request, 'main.html')


def my_view(request):
    users = ["Admin", "User", "Guest"]
    return render(request, 'main.html', {'users': users})



