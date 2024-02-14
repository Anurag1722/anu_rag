from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from myapp.models import Items
from myapp.serializers import ItemSerializer
from rest_framework import status

# Create your views here.

@api_view(["POST"])
def add_items(request):
    item=ItemSerializer(data=request.data)

    if Items.objects.filter(**request.data).exists():
        raise serializer.validationError("already exist")
    
    if item.is_valid():
        item.save()
        return Response(item.data)
    else:
        return Response(status=status.HTTP_404_FOUND)
    
    

@api_view(['GET'])
def view_items(request):
    if request.query_params:
        items=Items.objects.filter(**request.query_params.dict())
    else:
        items=Items.objects.all()
    if items:
        serializer=ItemSerializer(items,many=True)
        v={'data':serializer.data}
        return Response(v)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
@api_view(['POST'])    
def update_items(request,pk):
    item=Items.objects.get(pk=pk)
    data=ItemSerializer(instance=item,data=request.data)

    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
@api_view(['DELETE'])    
def delete_items(request,pk):
    item=Items.objects.get(pk=pk)
    item.delete()
    return Response(status=status.HTTP_404_NOT_FOUND)
    


    