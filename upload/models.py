from django.db import models

class Profile(models.Model):
   name = models.CharField(max_length = 50)
   picture = models.ImageField(upload_to = 'upload_file')

   class Meta:
      db_table = "profile"