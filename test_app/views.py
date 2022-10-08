from django.shortcuts import render

def index(request):
    context = {
        'message':'Bonjour',
    }
    return render(request,'test_app/index.html', context= context)


