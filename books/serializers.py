from rest_framework import serializers
from .models import Book


# used to convert a python object to json format. class based serializer has been used.
class bookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'Name', 'Author', 'Description', 'Reader')
