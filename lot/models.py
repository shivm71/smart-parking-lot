from django.db import models

# Create your models here.
class slot(models.Model):
    slot_id =  models.IntegerField(default=1)
    booked = models.BooleanField(default=False)
    reg_no = models.CharField(max_length=50, blank=True)
    level = models.IntegerField(default=1)
    parked_time = models.CharField(max_length=50, blank=True)
    # Park_time =  models.DateTimeField()
    def __str__(self):
        return str(self.id)

