from rest_framework import serializers
from .models  import Book


class BookSerializer(serializers.ModelSerializer):
    # review  = serializers.SerializerMethodField(method_name='get_review' , )
    class Meta:
        model = Book
        fields = "__all__"
