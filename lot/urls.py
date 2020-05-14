from django.urls import path

from . import views

app_name = 'lot'

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('all/', views.all, name='get_all_slot'),
    # ex: /polls/5/results/
    path('booked/', views.booked, name='get_booked_slot'),
    path('rpark/', views.randp, name='rand_park'),
    # ex: /polls/5/vote/
    path('available/', views.available, name='get_available_slot'),
    path('park/<int:pk>', views.park, name='park'),
    path('unpark/<int:pk>', views.unpark, name='unpark'),
    path('slot_info', views.slot_info, name='slot_info'),
    path('vehicle_info', views.vehicle_info, name='vehicle_info'),
]

# <li><a href="{% url 'lot:get_all_slot' %}">get All slots</a></li>
# <li><a href="{% url 'lot:get_booked_slot' %}">get All booked slots</a></li>
# <li><a href="{% url 'lot:get_available_slot' %}">get All Available slots</a></li>
# <li><a href="{% url 'lot:park' %}">Park</a></li>
# <li><a href="{% url 'lot:unpark' %}">Unpark</a></li>