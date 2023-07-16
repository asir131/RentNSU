from django.urls import path, re_path

from rent_product import views

urlpatterns=[
    path('', views.all_products, name='all_products'),
    path('add-product/', views.add_product, name='add_product'),
    path('my-products/', views.my_products, name='my_products'),
    path('view-product/', views.view_product, name='view_product'),
    path('my-requests/', views.my_requests, name='my_requests'),
    path('rent-product/<int:id>/', views.rent_product, name='rent_product'),
    path('update-request/', views.update_request, name='update_req'),
    path('delete-request/', views.delete_request, name='delete_req'),
    path('update-product/', views.update_product, name='update_product'),
    path('delete-product/', views.delete_product, name='delete_product'),
    path('rent-requests/', views.rent_requests, name='rent_requests'),
    path('approve-request/', views.approve_request, name='approve_rent'),
]