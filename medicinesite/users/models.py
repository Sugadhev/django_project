from django.db import models

class RegisterForm(models.Model):
    location = models.CharField(max_length=100, default="NA")
    medicinename = models.CharField(max_length=100,default="NA")
    medicinecategory = models.CharField(max_length=100,default="NA")
    symptoms = models.CharField(max_length=100,default="NA")
  

    class meta:
        db_table='doctor'

    def str(self):
        return self.name