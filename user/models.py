from django.db import models

# Create your models here.

class User(models.Model):

    stb_id = models.CharField(max_length=60)
    mac_addr = models.CharField(max_length=30)
    iptv_status_code = models.CharField(max_length=10)

    @classmethod
    def create(cls, stb_id, mac_addr, iptv_status_code):
         user = cls(stb_id=stb_id
                    , mac_addr=mac_addr
                    , iptv_status_code=iptv_status_code)
         return user
