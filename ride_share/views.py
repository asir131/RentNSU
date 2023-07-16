from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Create your views here.
from ride_share.forms import *
from ride_share.models import *


def all_vehicles(request):
    vehicles = Vehicle.objects.all()
    context = {
        'vehicles': vehicles
    }
    return render(request, 'ride_share/all_vehicles.html', context)


@login_required
def my_vehicles(request):
    vehicles = Vehicle.objects.filter(owner_id=request.user.id)
    context = {
        'vehicles': vehicles
    }
    return render(request, 'ride_share/my_vehicles.html', context)


def view_vehicle(request):
    vehicle = Vehicle.objects.filter(id=request.GET.get('vehicle_id')).first()
    context = {
        'vehicle': vehicle
    }
    return render(request, 'ride_share/vehicle.html', context)


@login_required
def add_vehicle(request):
    form = VehicleForm()
    if request.method == 'POST':
        form = VehicleForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.save(commit=False)
            data.owner_id = request.user.id
            data.save()
            messages.success(request, "Vehicle listed successfully")
            return redirect(my_vehicles)
    context = {
        'form': form
    }
    return render(request, 'ride_share/add_vehicle.html', context)


@login_required
def update_vehicle(request):
    vehicle = Vehicle.objects.filter(id=request.GET.get('vehicle_id')).first()
    if vehicle.owner != request.user:
        messages.error(request, "Unauthorized access")
        return redirect(my_vehicles)
    form = VehicleForm(instance=vehicle)
    if request.method == 'POST':
        form = VehicleForm(request.POST, request.FILES, instance=vehicle)
        if form.is_valid():
            form.save()
            messages.success(request, "Vehicle updated successfully")
            return redirect(my_vehicles)
    context = {
        'form': form
    }
    return render(request, 'ride_share/update_vehicle.html', context)


@login_required
def delete_vehicle(request):
    vehicle = Vehicle.objects.filter(id=request.GET.get('vehicle_id')).first()
    if vehicle.owner != request.user:
        messages.error(request, "Unauthorized access")
        return redirect(my_vehicles)
    vehicle.delete()
    messages.success(request, "Vehicle has been deleted successfully")
    return redirect(my_vehicles)


@login_required
def ride_vehicle(request, id):
    form = RideRequestForm()
    vehicle = Vehicle.objects.filter(id=id).first()

    if request.method == 'POST':
        if vehicle.owner == request.user:
            messages.error(request, "Unsuccessful attempt!")
            return redirect(my_vehicles)
        form = RideRequestForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.passenger_id = request.user.id
            data.vehicle_id = vehicle.id
            vehicle.save()
            data.save()
            messages.success(request, "Request for ride successfully")
            return redirect(all_vehicles)
    context = {
        'form': form,
        'vehicle': vehicle
    }
    return render(request, 'ride_share/ride_vehicle.html', context)


@login_required
def delete_request(request):
    ride = Ride.objects.filter(id=request.GET.get('rent_id')).first()
    if ride.passenger != request.user:
        messages.error(request, "Unauthorized access")
        return redirect(my_vehicles)
    ride.delete()
    messages.success(request, "Rent request cancelled successfully")
    return redirect(my_vehicles)


@login_required
def all_requests(request):
    rides = Ride.objects.filter(passenger=request.user)
    context = {
        'rides': rides
    }
    return render(request, 'ride_share/my_requests.html', context)


@login_required
def update_request(request):
    ride = Ride.objects.filter(id=request.GET.get('ride_id')).first()
    form = RideRequestForm(instance=ride)
    if request.method == 'POST':
        form = RideRequestForm(request.POST, instance=ride)
        if form.is_valid():
            form.save()
            messages.success(request, "Request updated successfully")
            return redirect(all_requests)
    context = {
        'form': form
    }
    return render(request, 'ride_share/update_request.html', context)


@login_required
def ride_requests(request):
    rides = Ride.objects.filter(vehicle__owner=request.user)

    context = {
        'rides': rides
    }
    return render(request, 'ride_share/ride_requests.html', context)


@login_required
def approve_request(request):
    ride = Ride.objects.filter(id=request.GET.get('ride_id')).first()

    if ride.is_approved:
        ride.is_approved = False
        messages.success(request, "Request disapproved successfully")
    else:
        ride.is_approved = True
        messages.success(request, "Request approved successfully")
    ride.save()
    return redirect('ride_requests')
