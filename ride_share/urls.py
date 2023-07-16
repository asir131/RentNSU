from django.urls import path, re_path

from ride_share import views

urlpatterns=[
    path('', views.all_vehicles, name='all_vehicles'),
    path('add-vehicle/', views.add_vehicle, name='add_vehicle'),
    path('my-vehicles/', views.my_vehicles, name='my_vehicles'),
    path('view-vehicle/', views.view_vehicle, name='view_vehicle'),
    path('all-requests/', views.all_requests, name='all_requests'),
    path('ride-vehicle/<int:id>/', views.ride_vehicle, name='ride_vehicle'),
    path('update-request/', views.update_request, name='update_request'),
    path('delete-request/', views.delete_request, name='delete_request'),
    path('update-vehicle/', views.update_vehicle, name='update_vehicle'),
    path('delete-vehicle/', views.delete_vehicle, name='delete_vehicle'),
    path('ride-requests/', views.ride_requests, name='ride_requests'),
    path('approve-request/', views.approve_request, name='approve_request'),
]