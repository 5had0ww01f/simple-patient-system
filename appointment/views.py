from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from database.models import patientData, nicknameTable, contactData, appointmentData, cureData
import datetime


# Create your views here.
@login_required
def appointment_index(request):

    nt = nicknameTable.objects.filter()
    nt = nt.extra(order_by = ['unique_id'])
    return render(request, 'appointment.html', {
    	'id_date':datetime.datetime.now().strftime("%Y%m%d"), 
    	'id_time':datetime.datetime.now().strftime("%H%M%S"),
    	'nicknameList':nt
    })
