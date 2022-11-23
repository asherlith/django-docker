from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, ListAPIView
from .models import Book
from .serializers import bookSerializer
from django.core.cache import cache
from rest_framework import status
from django.views.decorators.cache import cache_page


# class based views were used here.
class allBook(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = bookSerializer


# class based views were used here.
class Create(CreateAPIView):
    model = Book
    serializer_class = bookSerializer


# in api_view we define which type of requests can be sent.
@api_view(['GET'])
# @cache_page(100)
def Show(request, id):
    # if the book doesn't exist,404 status will be sent automatically.
    book = get_object_or_404(Book, id=id)
    if request.method == 'GET':
        # if the object is in the cache, get it from there,
        # otherwise get it from the database and bring it to the cache.
        if cache.get(id):
            book = cache.get(id)
        else:
            cache.set(book, id)
        serializer = bookSerializer(book)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['PUT', 'DELETE'])
def Change(request, id):
    book = get_object_or_404(Book, id=id)
    if request.method == 'PUT':
        serializer = bookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            # update the object both in the cache and database.
            cache.set(book, id)

            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    else:
        # delete the object both from the database and cache.
        cache.delete(id)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
