from django.urls import path
from . import views

urlpatterns=[

    path('hotels/',views.getHotels,name="getHotels"),
    path('hotels/<str:pk>',views.getHotel,name="getHotel"),
    path('hotel_search/',views.getHotelSearch,name="hotel_search"),
    path('filter_hotel_search/',views.getHotelFilters,name="filter_hotel_search"),


      path('hello/', views.hello_world, name='hello_world'),
]