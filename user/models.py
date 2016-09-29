from django.db import models

class Stb(models.Model):
    class Meta:
        db_table = 'STB'

    stb_id = models.CharField(max_length=60, primary_key=True)
    iptv_status_code = models.CharField(max_length=10)

class PhysicalStb(models.Model):
    class Meta:
        db_table = 'PHYSICAL_STB'

    stb = models.ForeignKey(Stb, related_name='stb')
    mac_address = models.CharField(max_length=20, primary_key=True)

