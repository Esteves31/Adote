from django.shortcuts import redirect

def home(request):
    if request.method == 'GET':
        return redirect('/auth/login')
