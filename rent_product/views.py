from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Create your views here.
from rent_product.forms import *
from rent_product.models import Rent, Product


def all_products(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'rent_product/all_products.html', context)


@login_required
def my_products(request):
    products = Product.objects.filter(owner_id=request.user.id)
    context = {
        'products': products
    }
    return render(request, 'rent_product/my_products.html', context)


def view_product(request):
    product = Product.objects.filter(id=request.GET.get('product_id')).first()
    context = {
        'product': product
    }
    return render(request, 'rent_product/product.html', context)


@login_required
def add_product(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.save(commit=False)
            data.owner_id = request.user.id
            data.save()
            messages.success(request, "Product listed successfully")
            return redirect(my_products)
    context = {
        'form': form
    }
    return render(request, 'rent_product/add_product.html', context)


@login_required
def update_product(request):
    product = Product.objects.filter(id=request.GET.get('product_id')).first()
    form = ProductForm(instance=product)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, "Product updated successfully")
            return redirect(my_products)
    context = {
        'form': form
    }
    return render(request, 'rent_product/update_product.html', context)


@login_required
def delete_product(request):
    product = Product.objects.filter(id=request.GET.get('product_id')).first()
    product.delete()
    messages.success(request, "Product has been deleted successfully")
    return redirect(my_products)


@login_required
def rent_product(request, id):
    form = RentRequestForm()
    product = Product.objects.filter(id=id).first()

    if request.method == 'POST':
        form = RentRequestForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.tenant_id = request.user.id
            data.product_id = product.id
            product.save()
            data.save()
            messages.success(request, "Rent product request successfully")
            return redirect(my_requests)
    context = {
        'form': form,
        'product': product
    }
    return render(request, 'rent_product/rent_product.html', context)


@login_required
def update_request(request):
    rent = Rent.objects.filter(id=request.GET.get('rent_id')).first()
    form = RentRequestForm(instance=rent)
    if request.method == 'POST':
        form = RentRequestForm(request.POST, instance=rent)
        if form.is_valid():
            form.save()
            messages.success(request, "Request updated successfully")
            return redirect(my_requests)
    context = {
        'form': form
    }
    return render(request, 'rent_product/update_request.html', context)


@login_required
def delete_request(request):
    rent = Rent.objects.filter(id=request.GET.get('rent_id')).first()
    rent.delete()
    messages.success(request, "Rent request cancelled successfully")
    return redirect(my_products)


@login_required
def my_requests(request):
    rents = Rent.objects.filter(tenant=request.user)
    context = {
        'rents': rents
    }
    return render(request, 'rent_product/my_requests.html', context)


@login_required
def rent_requests(request):
    rents = Rent.objects.filter(product__owner=request.user)
    context = {
        'rents': rents
    }
    return render(request, 'rent_product/rent_requests.html', context)


@login_required
def approve_request(request):
    rent = Rent.objects.filter(id=request.GET.get('rent_id')).first()

    if rent.is_approved:
        rent.is_approved = False
        messages.success(request, "Request disapproved successfully")
    else:
        rent.is_approved = True
        messages.success(request, "Request approved successfully")
    rent.save()
    return redirect('rent_requests')
