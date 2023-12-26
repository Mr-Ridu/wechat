from django.db import models
# Create your models here.
class room_details(models.Model):
    room_name = models.CharField(max_length=500)
    reffer_code = models.IntegerField()
    username = models.CharField(max_length=250)

    def __str__(self):
        return self.room_name

class messege_details(models.Model):
    m_user = models.CharField(max_length=250)
    messege = models.TextField()
    m_time = models.DateTimeField(null=True, blank=True)
    m_room = models.CharField(max_length=500)

    def __str__(self):
        return self.m_user