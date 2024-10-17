from django.shortcuts import render  , get_object_or_404
from .models import Book
from .filters   import  BookFilters
from .serializers import BookSerializer
from rest_framework import status
from rest_framework.response  import Response
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes



# get all book


@api_view(['GET'])
def get_all_book(request):
    # books = Book.objects.all()
    filter  =  BookFilters(request.GET , queryset=Book.objects.all().order_by('id'))
    count  = filter.qs.count()
    serializer =BookSerializer(filter.qs , many=True)
    return Response(serializer.data)
    # return Response({"Products : " :serializer.data , "Count :" : count})


# Search Product Book 
@api_view(['GET'])
def search_product_book_id(request , pk):
    book   =  get_object_or_404(Book,id=pk)
    serializer = BookSerializer(book , many=False)
    if serializer.data:
        return Response({"Product ":serializer.data})
    else:
        return Response({"detalis": "Not Found ....!"})


# Create Product Book 
# Create Produvt  IF  Login 
@api_view(['POST'])
@permission_classes([IsAuthenticated])#  يلي ما عامل تسجيل مارح يطلع البيانات عنده
def new_product(request):
    data = request.data
    serializer =  BookSerializer(data=data)
    if serializer.is_valid():
        product = Book.objects.create(**data , user=request.user)
        res = BookSerializer(product,many=False)
        return Response({"Products":res.data})
    else:
        return Response({"serializer":serializer.errors})


# Update Product Book  => Login (Auth)
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_product_book(request  ,pk):  
   
    book  = get_object_or_404(Book  , id =pk)
  
    if book.user != request.user :  #هاد الشخص من حقا يعدل  مثال الشخص مايصير يعدل على منتجات غيرو
        return Response({"Error" : "Sorry You Can  Not Update this Product  Book "} , status= status.HTTP_403_FORBIDDEN)
   
    book.name        = request.data['name']
    book.price       = request.data['price']
    book.category    = request.data['category']
    book.description = request.data['description']
    book.stock       = request.data['stock']
    book.cost        = request.data['cost']
    
    book.save()
    # Convert Data To Json 
    serializer = BookSerializer(book , many=False)
    return Response({"Book Product : ":serializer.data})
        


# Delete Book Product  => Login (Auth)

@api_view(['GET'])
@permission_classes([IsAuthenticated])# 
def delete_product_book(request , pk ):
    book  = get_object_or_404(Book , id=pk)
    if book.user != request.user:
        return Response({"error":"Sorry You Can not Delete this Product" },  status=status.HTTP_403_FORBIDDEN)   # request.user : الشخص يلي عامل ال تسجيل 
    book.delete()
    return Response({"Delete Product":"Delete Action  Done ...!"} , status=status.HTTP_200_OK)
