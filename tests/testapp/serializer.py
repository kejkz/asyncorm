from asyncorm.serializers import ModelSerializer
from tests.testapp.models import Book


class BookSerializer(ModelSerializer):

    class Meta:
        model = Book
        fields = ['name', 'content', 'kks']


class BookSerializer2(ModelSerializer):

    class Meta:
        model = Book
        fields = ['name', 'content', ]
