from django.contrib.auth import update_session_auth_hash
from django.db.models import query
from django.utils import timezone
from rest_framework import serializers, viewsets, status
from rest_framework import generics
from rest_framework.decorators import api_view, permission_classes, renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from .models import Book, Magazine, Company, Author, Basket, BasketItem, Promo, Genre
from .serializers import BookSerializer, MagazineSerializer, BasketItemSerializer, BasketSerializer, AuthorSerializer


# Create your views here.

# ListBook
class SearchBook(generics.ListAPIView):
    """
    This views lists all the books, 
    optionally filtering by author, genre and 
    title
    """

    serializer_class = BookSerializer

    # You don't need any permission to see the books

    def get_queryset(self):
        author = self.request.query_params.get('author', None)
        title = self.request.query_params.get('title', None)
        genre = self.request.query_params.get('genre', None)

        queryset = Book.objects.all()

        if author:
            queryset = queryset.filter(author__first_name__contains=author)
        if title:
            queryset = queryset.filter(title__contains=title)
        if genre:
            queryset = queryset.filter(genre__name__contains=genre)

        return queryset


# UpdateBook
class UpdateBook(generics.UpdateAPIView):
    """
    This view update books data 
    Only admins can do it
    """

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAdminUser]

    def update(self, request, *args, **kwargs):
        instance = self.get_object()

        title = request.data.get('title')
        desc = request.data.get('desc')
        price = request.data.get('price')

        data = {
            'title': title,
            'desc': desc,
            'price': price
        }

        serializer = self.get_serializer(instance, data, partial=True)
        serializer.is_valid(raise_exception=True)

        self.perform_update(serializer)

        return Response(serializer.data)


# Create Book
class CreateBook(generics.CreateAPIView):
    """
    Create a new book 
    Only admins can do it 
    """
    permission_classes = [IsAdminUser]

    serializer_class = BookSerializer
    queryset = Book.objects.all()


# Retrieve Book
class RetrieveBook(generics.RetrieveAPIView):
    """
    Gets a single book 
    Any user can do it 
    """

    serializer_class = BookSerializer
    queryset = Book.objects.all()


# Delete book
class DeleteBook(generics.DestroyAPIView):
    """
    Delete a single book
    Only admins can do it
    """

    permission_classes = [IsAdminUser]

    serializer_class = BookSerializer
    queryset = Book.objects.all()


# Magazine Search View
class SearchMagazine(generics.ListAPIView):
    """
    As the book search view, this view
    search Magazines, based on parameters 
    or not
    """

    serializer_class = MagazineSerializer

    def get_queryset(self):
        title = self.request.query_params.get('title', None)
        edition = self.request.query_params.get('edition', None)
        genre = self.request.query_params.get('genre', None)

        queryset = Magazine.objects.all()

        if title:
            queryset = queryset.filter(title__contains=title)

        if edition:
            queryset = queryset.filter(edition__lte=edition)

        if genre:
            queryset = queryset.filter(genre__contains=genre)

        return queryset


# UpdateMagazine
class UpdateMagazine(generics.UpdateAPIView):
    """
    This view update magazine data
    Only admins can do it 
    """

    permission_classes = [IsAdminUser]

    serializer_class = MagazineSerializer
    queryset = Magazine.objects.all()

    def update(self, request, *args, **kwargs):
        title = self.request.data.get('title')
        desc = self.request.data.get('desc')
        price = self.request.data.get('price')

        data = {
            'title': title,
            'desc': desc,
            'price': price
        }

        instance = self.get_object()
        serializer = self.get_serializer(instance, data, partial=True)

        self.perform_update(serializer)

        return Response(serializer.data)


# Create magazine
class CreateMagazine(generics.CreateAPIView):
    """
    This view creates a magazine
    Only admins can do it
    """

    permission_classes = [IsAdminUser]

    serializer_class = MagazineSerializer
    queyset = Magazine.objects.all()


# Retrieve magz
class RetrieveMagazine(generics.RetrieveAPIView):
    """
    Gets a single magazine
    Anyone can do it 
    """

    serializer_class = MagazineSerializer
    queryset = Magazine.objects.all()


# Delete magz
class DeleteMagazine(generics.DestroyAPIView):
    """
    Delete a single magazine
    Only admins can do it
    """

    permission_classes = [IsAdminUser]

    serializer_class = MagazineSerializer
    queryset = Magazine.objects.all()


# ListAuthors
class SearchAuthor(generics.ListAPIView):
    """
    Search an author based in a str
    wich author's first name can start with
    Any user can do it
    """

    serializer_class = AuthorSerializer

    def get_queryset(self):
        input = self.request.query_params.get('name')

        queryset = Author.objects.all()

        if input:
            queryset = queryset.filter(first_name__starts_with=input)

        return queryset


# BUY
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def buy_item(request):
    """
    In this view, a type of item is specified
    and it is put in the user's basket
    """
 
    flag = True
    
    # Gets the type of the item
    item_type = request.data.get('type')

    if not item_type:
        return Response(data={'error': 'Item type not specidied'}, status=status.HTTP_400_BAD_REQUEST)

    if item_type == 'm':
        item_queryset = Magazine.objects.all()
    else:
        item_queryset = Book.objects.all()
        item_type = 'b'

    item_pk = request.data.get('id')

    item_queryset = item_queryset.filter(pk=int(item_pk)).first()
    if not item_queryset:
        return Response(data={'error': 'Item doesn\'t exists'}, status=status.HTTP_400_BAD_REQUEST)

    # Defines the current basket item
    for b in BasketItem.objects.all():
        # BasketItem already exists!
        if b.item_pk == item_pk and b.item_type == item_type:
            return Response(data={'error': 'Item is already on basket!'}, status=status.HTTP_400_BAD_REQUEST)

    # Get Basket
    basket = Basket.objects.all().filter(user=request.user).first()

    if Promo.objects.all().count() == 0:
        promo = Promo(tax=4.50, finish=timezone.now())
        promo.save()
    else:
        promo = Promo.objects.first()

    if not basket:
        flag = False
        basket = Basket(
            user=request.user,
            promo=promo,
            final_price=0.00
        )
    else:
        flag = True

    if flag:
        basket.final_price += item_queryset.price
    else:
        basket.final_price += float(item_queryset.price)
    basket.save()

    # New basket item
    data_bi = {
        'item_pk': item_queryset.pk,
        'item_type': item_type,
        'basket': basket.pk
    }

    serializer = BasketItemSerializer(data=data_bi)

    if serializer.is_valid():
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)

    return Response(data={'error': 'Basket item not created'}, status=status.HTTP_400_BAD_REQUEST)
