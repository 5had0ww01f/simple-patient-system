from django.db import models


class patientData(models.Model):
    unique_id = models.CharField(u'unique_id', max_length=15, unique=True, null=False)
    location = models.CharField(u'location', max_length=5, default='-') #TY,SL,etc
    gender = models.CharField(u'gender', max_length=10, default='-') # Male/Female
    id_card_number = models.CharField(u'id_card_number', max_length=15, default='-') # A123456789
    birthday = models.CharField(u'birthday', max_length=15, default='-') # 1955-05-05
    bloodtype = models.CharField(u'bloodtype', max_length=10, default='-') # AB
    mobile1 = models.CharField(u'mobile1', max_length=14, default='-') # 0911223445
    mobile2 = models.CharField(u'mobile2', max_length=14, default='-') # 0911223445
    telephone1 = models.CharField(u'telephone1', max_length=14, default='-') # 04-1234567
    telephone2 = models.CharField(u'telephone2', max_length=14, default='-') # 04-1234567
    is_alive = models.CharField(u'is_alive', max_length=10, default=True) # Alive/Dead
    def __unicode__(self):
        return self.unique_id

class nicknameTable(models.Model):
    unique_id = models.CharField(u'unique_id', max_length=15)
    nickname = models.CharField(u'nickname', max_length=50, null=False)
    is_new = models.IntegerField(u'is_new', default=1)

    def __unicode__(self):
        return self.unique_id

class contactData(models.Model):
    home_id = models.CharField(u'home_id', max_length=15, null=False, unique=True)
    address = models.CharField(u'address', max_length=100, default='-')
    telephone = models.CharField(u'telephone', max_length=14, default='-')
    host = models.CharField(u'host', max_length=100, default='-')
    family_stats = models.CharField(u'family_stats', max_length=500, default='-')
    description = models.CharField(u'description', max_length=3000, default='-')
    remark = models.CharField(u'remark', max_length=3000, default='-')
    def __unicode__(self):
        return self.home_id

class appointmentData(models.Model):
    code = models.CharField(u'code', max_length=10, default='19700101')
    unique_id = models.CharField(u'unique_id', max_length=15)
    subject = models.CharField(u'subject', max_length=10, default='-')
    bloodpressure = models.CharField(u'bloodpressure', max_length=10, default='-')
    bloodsugar = models.CharField(u'bloodsugar', max_length=10, default='-')
    height = models.CharField(u'height', max_length=10, default='-')
    weight = models.CharField(u'weight', max_length=10, default='-')
    remark = models.CharField(u'remark', max_length=3000, default='-')
    log_id = models.CharField(u'log_id', max_length=30, default='-') #time(0)_uid
    is_done = models.IntegerField(u'is_done', default=0)  # -1 = no show / 0 = not yet / 1 = done
    timeDate = models.CharField(u'timeDate', max_length=8, default='19700101') #20160101
    timeTime = models.CharField(u'timeTime', max_length=6, default='000000') #080808

    def __unicode__(self):
        return self.unique_id

class cureData(models.Model):
    log_id = models.CharField(u'log_id', max_length=30, default='-') #time(0)_uid
    unique_id = models.CharField(u'unique_id', max_length=15, null=False, default='DEFAULT')
    timeDate = models.CharField(u'timeDate', max_length=8, default='19700101')  # 20160101
    timeTime = models.CharField(u'timeTime', max_length=6, default='000000')  # 080808
    problem_tmp = models.CharField(u'problem_tmp', max_length=3000, default='-')
    solution_tmp = models.CharField(u'solution_tmp', max_length=3000, default='-')
    medicine_tmp = models.CharField(u'medicine_tmp', max_length=3000, default='-')
    medicine_tmp_appendix = models.CharField(u'medicine_tmp_appendix', max_length=3000, default='無')
    remark = models.CharField(u'remark', max_length=3000, default='-')
    subject = models.CharField(u'subject', max_length=10, default='-')
    is_taken = models.IntegerField(u'is_taken', default=0)  # -1 = no show / 0 = not yet / 1 = done
    def __unicode__(self):
        return self.log_id

class medicineData(models.Model):
    medicine_name = models.CharField(u'medicine_name', max_length=50, default='-')
    medicine_expiry = models.CharField(u'medicine_expiry', max_length=10, default='1970-01-01')
    medicine_unit = models.CharField(u'medicine_unit', max_length=10, default='-')
    medicine_count = models.IntegerField(u'medicine_count', default=0)
    def __unicode__(self):
        return self.medicine_count