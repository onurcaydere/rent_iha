from django.db import models

# Create your models here.

class iha_info(models.Model):
    iha_marka=models.TextField()
    iha_model=models.TextField()
    iha_agr=models.FloatField()
    iha_kat=models.TextField()
    iha_fiyat=models.FloatField()
class kira_info(models.Model):
    iha_marka=models.TextField(default="")
    iha_model=models.TextField(default="")
    iha_agr=models.FloatField(default=0.0)
    iha_kat=models.TextField(default="")
    iha_fiyat=models.FloatField(default=0.0)
    iha_kullanıcı=models.TextField(default="")
