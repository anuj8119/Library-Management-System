from django.shortcuts import render
from rest_framework.response import Response
from .models import Books
from rest_framework.views import APIView
from .serializers import BookSerializer
# Create your views here.

class BooksView(APIView):
    def get(self, request):
        try: 
            books = Books.objects.all()
            book_serializer = BookSerializer(books, many=True)
            return Response({
                'success': True, 
                'payload': book_serializer.data
                })
        except:
            return Response({
                'success': False,
                'message': 'No Books Found'
                })