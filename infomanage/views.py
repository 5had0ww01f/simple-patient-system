from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from database.models import patientData, nicknameTable, contactData, appointmentData, cureData

# Create your views here.

@login_required
def infomanage_index(request):

	nt = nicknameTable.objects.filter()
	nt = nt.extra(order_by = ['unique_id'])
	return render(request,'infomanage.html',{
		'nicknameList': nt,
		'patientData': patientData.objects.filter()
	})
