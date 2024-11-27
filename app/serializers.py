from rest_framework import serializers
from .models import Student, StuBook, StuReview

# Review Serializer
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = StuReview
        fields = ['id', 'r_text']

# Book Serializer with nested reviews
class BookSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = StuBook
        fields = ['id', 'title', 'reviews']

# Author Serializer with nested books and reviews
class StudentSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Student
        fields = ['id', 'name', 'Address', 'books']