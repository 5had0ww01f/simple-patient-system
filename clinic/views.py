from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from database.models import patientData, nicknameTable, contactData, appointmentData, cureData, medicineData

# Create your views here.
@login_required
def clinic_index(request, subject):
    return render(request, 'clinic.html', {
    	'subject':subject,
    	'M_list': appointmentData.objects.filter(subject="M"),
    	'M_waitCount': appointmentData.objects.filter(subject="M", is_done=0).count(),
    	'DEN_waitCount': appointmentData.objects.filter(subject="DEN", is_done=0).count(),
		'DEN_list': appointmentData.objects.filter(subject="DEN"),
		'nicknameTable': nicknameTable.objects.filter(),
        'cureHistory': cureData.objects.filter(),
        'medicine': medicineData.objects.filter(),
    })

