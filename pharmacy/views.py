from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from database.models import cureData, nicknameTable

# Create your views here.
@login_required
def pharmacy_index(request):
    return render(request, 'pharmacy.html', {
    	'waitList':cureData.objects.filter(is_taken=0),
    	'nicknameTable':nicknameTable.objects.filter(),
    })