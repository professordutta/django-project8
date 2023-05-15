from django.db import models

# Create your models here.

class Mriic(models.Model):
    emp_id = models.IntegerField(primary_key=True)
    emp_name = models.CharField(max_length=30)
    emp_age = models.CharField(max_length=30)
    def __str__(self):
        return self.emp_name
