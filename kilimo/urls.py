from django.urls import path
from . import views

urlpatterns = [
    # CRUD URLs
    path('add-product/', views.add_product, name='add_product'),
    path('edit-product/<int:id>/', views.edit_product, name='edit_product'),
    path('delete-product/<int:id>/', views.delete_product, name='delete_product'),
    path('view-products/', views.view_products, name='view_products'),
    path('insert-data/', views.insert_data, name='insert_data'),

    # Dropdown URLs
    path('fertilizers/', views.fertilizers, name='fertilizers'),
    path('farming-tools/', views.farming_tools, name='farming_tools'),
    path('pesticides/', views.pesticides, name='pesticides'),
    path('irrigation-equipments/', views.irrigation_equipments, name='irrigation_equipments'),
    path('livestock-supply/', views.livestock_supply, name='livestock_supply'),

    # Other Views
    path('', views.home, name='home'),
    path('subscribe/', views.subscribe, name='subscribe'),
    path('blog/', views.blog, name='blog'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('services/', views.services, name='services'),
    path('customers/', views.customers, name='customers'),
    path('blog-details/', views.blog_details, name='blog_details'),
    path('layout/', views.layout, name='layout'),
    path('newsletter-subscription/', views.newsletter_subscription, name='newsletter_subscription'),
    path('search-results/', views.search_results, name='search_results'),

]


