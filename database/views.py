from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from database.models import patientData, nicknameTable, contactData, appointmentData, cureData, medicineData
import datetime


# Create your views here.


@login_required
def addPatient(request):
    description = None;
    if request.GET.get('command'):

############################# 新增病患

        if str(request.GET.get('command')) == "add":
            req = "add"
            if request.GET.get('uid'):
                req = "edit"
                data_record = patientData.objects.filter(unique_id=request.GET.get('uid'))

            print("Add new patient.")
            if request.GET.get('location') and description == None:
                location = simpleParse(request.GET.get('location').upper());
                if len(location) < 7 and location.isalpha() and req == "add":
                    assignID = location + "%06d" % (patientCount(location) + 1)
                elif req == "edit": assignID = request.GET.get('uid')
                else:
                    description = "Bad location"
            else:
                if description == None: description = "Empty location"

            if request.GET.get('name') and description == None:
                name = simpleParse(request.GET.get('name'))
                if req == "edit": nicknameTable.objects.create(unique_id=assignID, nickname=name, is_new=0)
            else:
                if description == None and req == "add": description = "Empty name"


            if request.GET.get('id') and description == None:
                get_id = simpleParse(request.GET.get('id').upper());
                if len(get_id) == 10 and location.isalnum() and idValidate(get_id) == True:
                    get_id = simpleParse(request.GET.get('id').upper())
                    if req == "edit": data_record.update(id_card_number=get_id)
                else:
                    get_id = "-"
            else:
                if description == None: get_id = "-"

            print("Assign ID: " + assignID)

            if request.GET.get('gender') and description == None:
                gender = simpleParse(request.GET.get('gender'))
                if gender == "Male" or gender == "Female" or gender == "Other":
                    gender = simpleParse(request.GET.get('gender'))
                else:
                    description = "Bad gender"
            else:
                if description == None: description = "Empty gender"

            birthday = ""
            if request.GET.get('birthday') and description == None:
                birthday = simpleParse(request.GET.get('birthday'))
                if len(birthday)==10:
                    birthday = simpleParse(request.GET.get('birthday'))
                    if req == "edit": data_record.update(birthday=birthday)
                else:
                    description = "Bad birthday"

            if req == "edit":
                data_record.update(gender=gender)
                if request.GET.get('bloodtype') != "(Unknown)": data_record.update(bloodtype=request.GET.get('bloodtype'))

            if description == None:
                if req == "add":
                    data_record = patientData.objects.create(unique_id=assignID, location=location, gender=gender, birthday=birthday)
                    name_record = nicknameTable.objects.create(unique_id=assignID, nickname=name, is_new=1)
                    print(data_record.unique_id)
                    print(name_record.unique_id)
                    if data_record.unique_id != None and name_record.unique_id != None and data_record.unique_id == name_record.unique_id:
                        return render(request, 'returnpage.html', {'error': 0, 'description': description});
                        return HttpResponse(
                            "{\"error\":0, \"description\":\"success\", \"unique_id\":\"" + name_record.unique_id + "\"}")
                    else:
                        description = "Create error"
                else: return render(request, 'returnpage.html', {'error': 0, 'description': description});

######################### # 掛號 TODO: Security Check

        elif str(request.GET.get('command')) == "appointment":

            if request.GET.get('code') and description == None:
                app_code = int(simpleParse(request.GET.get('code')));
            else:
                if description == None: description = "Empty code"

            if request.GET.get('unique_id') and description == None:
                app_unique_id = simpleParse(request.GET.get('unique_id'));
            else:
                if description == None: description = "Empty unique_id"

            if request.GET.get('subject') and description == None:
                app_subject = simpleParse(request.GET.get('subject').upper())
            else:
                if description == None: description = "Empty subject"

            if request.GET.get('bloodpressure') and description == None:
                app_bloodpressure = simpleParse(request.GET.get('bloodpressure'))
            else:
                app_bloodpressure = 0

            if request.GET.get('bloodsugar') and description == None:
                app_bloodsugar = int(simpleParse(request.GET.get('bloodsugar')))
            else:
                app_bloodsugar = 0

            if request.GET.get('weight') and description == None:
                app_weight = int(simpleParse(request.GET.get('weight')))
            else:
                app_weight = 0

            if request.GET.get('height') and description == None:
                app_height = int(simpleParse(request.GET.get('height')))
            else:
                app_height = 0

            if request.GET.get('remark') and description == None:
                app_remark = simpleParse(request.GET.get('remark'));
            else:
                app_remark = "None"

            if description == None:

                date = datetime.datetime.now().strftime("%Y%m%d")
                time = datetime.datetime.now().strftime("%H%M%S")
                log_id = date + time + "_" + app_unique_id;
                appointment_rec = appointmentData.objects.create(
                    code=app_code,
                    unique_id=app_unique_id,
                    subject=app_subject,
                    bloodpressure=app_bloodpressure,
                    bloodsugar=app_bloodsugar,
                    height=app_height,
                    weight=app_weight,
                    remark=app_remark,
                    log_id=log_id,
                    timeDate=datetime.datetime.now().strftime("%Y%m%d"),
                    timeTime=datetime.datetime.now().strftime("%H%M%S"),
                    is_done=0
                )

                if appointment_rec.unique_id != None:
                    app_count = appointmentData.objects.filter(code=app_code).count()
                    return render(request, 'returnpage.html', {'error': 0, 'description': description});
                else:
                    description = "Create error"

###################### 診療

        elif str(request.GET.get('command')) == "cure":
            if request.GET.get('log_id') and description == None:
                cure_log_id = simpleParse(request.GET.get('log_id'));
            else:
                if description == None: description = "未選擇病患"

            if request.GET.get('subject') and description == None:
                cure_subject = request.GET.get('subject')
            else:
                if description == None: description = "Empty subject"

            if request.GET.get('problem_tmp') and description == None:
                cure_problem_tmp = simpleParse(request.GET.get('problem_tmp'));
            else:
                if description == None: description = "主述為空"

            if request.GET.get('solution_tmp') and description == None:
                cure_solution_tmp = simpleParse(request.GET.get('solution_tmp'));
            else:
                if description == None: description = "診斷為空"

            if request.GET.get('medicine_tmp') and description == None:
                cure_medicine_tmp = simpleParse(request.GET.get('medicine_tmp'));
            else:
                if description == None: description = "藥物為空"

            if request.GET.get('medicine_tmp_appendix') and description == None:
                cure_medicine_tmp_appendix = simpleParse(request.GET.get('medicine_tmp_appendix'));
            else:
                cure_medicine_tmp_appendix = "無"

            if request.GET.get('remark') and description == None:
                cure_remark = simpleParse(request.GET.get('remark'))
            else:
                cure_remark = "無"

            if description == None:
                if cureData.objects.filter(log_id=cure_log_id).count() == 0:

                    if cure_medicine_tmp == '本案未開藥': print("wwwwwwwwwww")
                    else:
                        splt = cure_medicine_tmp.split("<br>")
                        for s in splt: 
                            if len(s.split('_')[0])>0:
                                use_id = s.split('_')[0].split('*')[0]
                                use_num = s.split('_')[0].split('*')[1]
                                med = medicineData.objects.filter(id=use_id)
                                medget = medicineData.objects.get(id=use_id)
                                med.update(medicine_count=medget.medicine_count-int(use_num))

                    appData = appointmentData.objects.get(log_id=cure_log_id)
                    cure_record = cureData.objects.create(
                        log_id=cure_log_id,
                        problem_tmp=cure_problem_tmp,
                        solution_tmp=cure_solution_tmp,
                        medicine_tmp=cure_medicine_tmp,
                        medicine_tmp_appendix = cure_medicine_tmp_appendix,
                        remark=cure_remark,
                        timeDate = appData.timeDate,
                        timeTime = appData.timeTime,
                        unique_id = appData.unique_id,
                        subject = cure_subject,
                        is_taken=0
                    )
                    if cure_record.log_id != None:
                        to_remove = appointmentData.objects.get(log_id=cure_record.log_id)
                        print("Finish: " + to_remove.unique_id)
                        to_remove.is_done = 1
                        to_remove.save()
                        return render(request, 'returnpage.html', {'error': 0, 'description': description});
                    else:
                        description = "Send error"
                else:
                    description = "Already saved"

###################### 拿藥

        elif str(request.GET.get('command')) == "taken":  
            print("Medicine taken.")
            if request.GET.get('log_id') and description == None:
                log_id = simpleParse(request.GET.get('log_id'));
            else:
                description = "Empty log_id"

            if description == None:
                medicine = cureData.objects.get(log_id=log_id)
                medicine.is_taken = 1
                medicine.save()
                return render(request, 'returnpage.html', {'error': 0, 'description': description});
                return HttpResponse(
                    "{\"error\":0, \"description\":\"success\", \"log_id\":\"" + medicine.log_id + "\"}")

##################### ADD MEDICINE DATA

        elif str(request.GET.get('command')) == "add_medicine":
            print("adding medicine")
            if request.GET.get('medicine_name') and description == None:
                medicine_name = simpleParse(request.GET.get('medicine_name'));
            else:
                description = "Empty medicine_name"

            if request.GET.get('medicine_unit') and description == None:
                medicine_unit = simpleParse(request.GET.get('medicine_unit'));
            else:
                description = "Empty medicine_unit"

            if request.GET.get('medicine_count') and description == None:
                medicine_count = simpleParse(request.GET.get('medicine_count'));
            else:
                description = "Empty medicine_count"

            if request.GET.get('medicine_expiry') and description == None:
                medicine_expiry = simpleParse(request.GET.get('medicine_expiry'));
            else:
                description = "Empty medicine_expiry"

            if description == None:
                medicine = medicineData.objects.create(medicine_name=medicine_name, medicine_unit=medicine_unit, medicine_count=medicine_count, medicine_expiry=medicine_expiry)
                #medicine.is_taken = 1
                #medicine.save()
                return render(request, 'returnpage.html', {'error': 0, 'description': description});
                return HttpResponse(
                    "{\"error\":0, \"description\":\"success\", \"log_id\":\"" + medicine.log_id + "\"}")

######################### ADD 

        elif str(request.GET.get('command')) == "add_medicine_multi":
            print("adding medicine multi line")
            if request.GET.get('medicine_list') and description == None:
                medicine_name = simpleParse(request.GET.get('medicine_list'));
                rawlist = request.GET.get('medicine_list').strip().split('\r\n')
                #print(rawlist)
                for a in rawlist:
                    print(a.split(',')[0].encode())
                    medicine = medicineData.objects.create(medicine_name=a.split(',')[0], medicine_unit=a.split(',')[2], medicine_count=a.split(',')[1])           
            else:
                description = "Empty medicine_name"

            return render(request, 'returnpage.html', {'error': 0, 'description': description});
            return HttpResponse(
                    "{\"error\":0, \"description\":\"success\", \"log_id\":\"" + medicine.log_id + "\"}")

######################### EDIT Pinfo

        elif str(request.GET.get('command')) == "edit_pinfo":

            if request.GET.get('nickname') and request.GET.get('log_id') and description == None:
                new_name = simpleParse(request.GET.get('nickname'));
                logId = simpleParse(request.GET.get('log_id'));
                    
                pinfo = nicknameTable.objects.create(unique_id=logId, nickname=new_name, is_new=0)           
            
            else:
                description = "Empty nickname / Wrong Id"

            return render(request, 'returnpage.html', {'error': 0, 'description': description});
            return HttpResponse(
                    "{\"error\":0, \"description\":\"success\", \"log_id\":\"" + pinfo.log_id + "\"}")


######################### Del patient

        elif str(request.GET.get('command')) == "del_patient":

            if request.GET.get('log_id') and description == None:
                log_id = simpleParse(request.GET.get('log_id'));
                tmp = appointmentData.objects.filter(log_id=log_id)
                tmp.update(is_done=1)
            
            else:
                description = "Empty Id"

            return render(request, 'returnpage.html', {'error': 0, 'description': description});
            return HttpResponse(
                    "{\"error\":0, \"description\":\"success\", \"log_id\":\"" + pinfo.log_id + "\"}")

                                
################## END OF SWITCH SECTION #############

    else:
        description = "Empty command"

    if description == None:
        print("No error but you shouldn't see this.")
    else:
        return render(request, 'returnpage.html', {'error': 1, 'description': description});
        return HttpResponse("{\"error\":1, \"description\":\"" + description + "\"}")




###=======================Not View====================##
def simpleParse(plaintext):
    rp = plaintext
    return rp.replace('<', '〈').replace('>', '〉').replace('\'', '`').replace('\"', '〝').replace('\n', '<br>');


def idValidate(idnum):
    return True


def patientCount(location='TY'):
    count = patientData.objects.filter(location=location).count()
    return count
