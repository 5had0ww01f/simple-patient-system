from django.shortcuts import render

# Create your views here.

def dashboard_index(request):
    return render(request, 'index.html', {});

def google_check(request):
    return render(request, 'google9eb2f55447b43980.html', {})
