from django.shortcuts import render ,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from .models import slot
from django.urls import reverse
from datetime import datetime
from  . import pparse as p


# Create your views here.
def index(request):
    return render(request, 'iot/index.html')
    

def all(request):
    latest_question_list = slot.objects.order_by('slot_id')
    context = {'list': latest_question_list,'toshowbooked' : True,'toshowunbooked' : False}
    return render(request, 'iot/table.html',context)

def booked(request): 
    latest_question_list = slot.objects.order_by('slot_id').filter(booked=True)
    context = {'list': latest_question_list,'toshowbooked' : True,'toshowunbooked' : False}
    print(type(context),latest_question_list)
    return render(request, 'iot/table.html',context)
    return HttpResponse("some error")
    

def available(request):
    latest_question_list = slot.objects.order_by('slot_id').filter(booked=False)
    context = {'list': latest_question_list,'toshowbooked' : False,'toshowunbooked' : True}
    # print(type(context),latest_question_list)
    return render(request, 'iot/table.html',context)
    return HttpResponse("some error")
def park(request,pk):
    print(pk)
    carslot = get_object_or_404(slot, pk=pk)
    print(carslot,"obj")
    if carslot :
        carslot.reg_no = request.POST['name']
        carslot.booked = True
        carslot.parked_time = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
        carslot.save()
    greet = p.out(request.POST['name'])
    context = {'list': [carslot],'greet':greet,'toshowbooked' : False,'toshowunbooked' : True}
    return render(request, 'iot/table.html',context)    
    # return HttpResponseRedirect(reverse('lot:get_booked_slot'))    

    return HttpResponse("chal gya")  
def unpark(request,pk):
    print(pk)
    carslot = get_object_or_404(slot, pk=pk)
    print(carslot,"obj")
    if carslot :
        carslot.reg_no = "--"
        carslot.booked = False
        carslot.parked_time = "NO CAR PARKED YET"
        carslot.save()
    return HttpResponseRedirect(reverse('lot:get_booked_slot'))  
def randp(request):
    level = request.POST["level"]
    name = request.POST["name"]
    slotlist = slot.objects.order_by('slot_id').filter(booked=False,level = level)[0]
    slotlist.booked = True
    slotlist.reg_no = name
    slotlist.parked_time = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
    slotlist.save()
    print(slotlist)
    greet = p.out(name)
    context = {'list': [slotlist],'greet':greet,'toshowbooked' : False,'toshowunbooked' : True}
    return render(request, 'iot/table.html',context)
def slot_info(request):
    slot_id = request.POST["level"]
    slotlist = slot.objects.order_by('slot_id').filter(slot_id = slot_id)
    context = {'list': slotlist,'toshowbooked' : False,'toshowunbooked' : True}
    return render(request, 'iot/table.html',context)
def vehicle_info(request):
    name = request.POST["name"]
    slotlist = [ slot.objects.all().filter(reg_no=name)[0]]
    context = {'list': slotlist,'toshowbooked' : False,'toshowunbooked' : True}
    return render(request, 'iot/table.html',context)       
     