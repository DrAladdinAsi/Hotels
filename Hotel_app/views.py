from rest_framework.response import Response
from rest_framework.decorators import api_view 
from .serializers import *
from .models import *
from django.shortcuts import render




#for testing
def hello_world(request):
    return render(request, 'hello_world.html')




#for the hotel

@api_view(['GET'])
def getHotels(request):
    hotels = Hotel.objects.all()
    serializer = HotelSerializer(hotels , many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getHotel(request,pk):
    hotel=Hotel.objects.get(id=pk)
    serializer=HotelSerializer(hotel,many=False)
    return Response(serializer.data)


@api_view(['GET'])
def getHotelSearch(request):
    query=request.query_params.get('q')
    if query is "":
        result=Hotel.objects.all()
        
    else:
        print('query : ',query)
        
    result=Hotel.objects.filter(city__icontains=query)

    print(result)
    serializer=HotelSerializer(result,many=True)
    return Response(serializer.data)



@api_view(['POST'])
def getHotelFilters(request):
    H_type=request.data.get('H_type')
    station_dest=request.data.get('stations_dest')
    price=request.data.get('price')
    bed_num=request.data.get('bed_num')
    
    
    queryset = Hotel.objects.all()

    # Dynamically build the query based on available data
    if H_type:
        queryset = queryset.filter(h_type=H_type)

    if station_dest:
        queryset = queryset.filter(stations_dest__lte=station_dest)

    if price:
        queryset = queryset.filter(price__lte=price)

    if bed_num:
        queryset = queryset.filter(bed_num__gte=bed_num)

    serializer=HotelSerializer(queryset,many=True)
    return Response(serializer.data)









