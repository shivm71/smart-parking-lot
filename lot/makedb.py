from lot.models import slot
import random
from datetime import datetime
date_time = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
print(len(slot.objects.all()))
slot.objects.all().delete()
# Ticket.objects.all().delete()
for i in range(1,31):
   #   if random.randint(0,1) == 1:   
   #      slott,created = slot.objects.get_or_create(parked_time = "NO Vehile Parked Yet" , slot_id = i,level=random.randint(1,3),booked = True)
   #   else:
   #      slott,created = slot.objects.get_or_create(parked_time = "NO Vehile Parked Yet" , slot_id = i,level=random.randint(1,3),booked = False)
     slott,created = slot.objects.get_or_create(parked_time = "NO Vehile Parked Yet" , slot_id = i,level=random.randint(1,3),booked = False)
     pass


print("vneihg")     
        