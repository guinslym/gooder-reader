from rest_framework import serializers
from .models import *

from books.serializers import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('pk', 'username', 'email')

class GRUserSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    shelves = ShelfSerializer(many=True)
    books = BookSerializer(many=True)

    class Meta:
        model = GRUser
        fields = ('pk', 'user', 'first_name', 'last_name', 'shelves', 'books')
