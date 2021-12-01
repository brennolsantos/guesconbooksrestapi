from django.db import models
from django.db.models.fields import DateField
from django.contrib.auth import get_user_model

User = get_user_model()

# COMPANY


class Company(models.Model):
    """
    The model of Company of publishing. The
    books and Magazines can be linked to it
    """

    name = models.CharField('Name', max_length=100, blank=True)
    desc = models.TextField('Desc', max_length=1200, blank=True)
    picture = models.ImageField('Photo', upload_to='companies/', null=True)
    creat_date = models.DateField('Created', auto_now_add=True, blank=True)
    update_date = models.DateField('Updated', blank=True, null=True)

    class Meta:
        verbose_name = 'Companie'
        verbose_name_plural = 'Companies'
        ordering = ['name']


# AUTHOR
class Author(models.Model):
    """
    The model of author, which
    one or more books are linked to 
    """

    first_name = models.CharField('First Name', max_length=100, blank=True)
    last_name = models.CharField('Last Name', max_length=100, blank=True)
    desc = models.TextField('Desc', max_length=1200, blank=True)
    birth_date = DateField('Birth', blank=True, null=True)
    picture = models.ImageField('Photo', upload_to='authors/', null=True)

    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'
        ordering = ['first_name']


# GENRE
class Genre(models.Model):
    """
    The model of Genre, wich
    represents book or magazine genre, like:

    - Terror
    - Action
    - Drama
    """

    name = models.CharField('Genre', max_length=100, blank=True)
    desc = models.TextField('Desc', max_length=1200, blank=True)

    class Meta:
        verbose_name = 'Genre'
        verbose_name_plural = 'Genres'
        ordering = ['name']

# BOOK


class Book(models.Model):
    """
    The model Book
    wich has descriptions of a book, linked
    to an author and a company
    """

    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

    title = models.CharField('Title', max_length=100, blank=True)
    desc = models.TextField('Desc', max_length=1200, blank=True)
    num_pages = models.PositiveIntegerField('Number of Pages', null=True)
    price = models.DecimalField(
        'Price', max_digits=10, decimal_places=2, null=True)
    cover = models.ImageField('Cover', upload_to='books/', null=True)

    publish_date = models.DateTimeField('Published', null=True)
    creat_date = models.DateField('Created', auto_now_add=True)
    update_date = models.DateTimeField('Updated', auto_now=True, null=True)

    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'
        ordering = ['title', 'author']


# MAGAZINE
class Magazine(models.Model):
    """
    Class model magazine
    Wich represents a magazine with its information
    """

    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

    title = models.CharField('Title', max_length=100, blank=True)
    edition = models.PositiveSmallIntegerField('Edition', null=True)
    desc = models.TextField('Desc', max_length=1200, blank=True)
    num_pages = models.PositiveIntegerField('Number of pages', null=True)
    price = models.DecimalField(
        'Price', max_digits=10, decimal_places=2, null=True)
    cover = models.ImageField('Cover', upload_to='magazine', null=True)

    publish_date = models.DateTimeField('Published', null=True)
    creat_date = models.DateField('Created', auto_now_add=True)
    update_date = models.DateTimeField('Updated', auto_now=True, null=True)

    class Meta:
        verbose_name = 'Magazine'
        verbose_name_plural = 'Magazines'
        ordering = ['title', '-edition']


# PROMO
class Promo(models.Model):
    """
    The promo model
    A model wich describes a % of discount, wich 
    a basket is linked to
    """

    tax = models.DecimalField('Discount', max_digits=4,
                              decimal_places=2, blank=True)
    start = models.DateTimeField('Start date', auto_now_add=True)
    finish = models.DateTimeField('Finish', null=False)

    class Meta:
        verbose_name = 'Promo'
        verbose_name_plural = 'Promos'
        ordering = ['start']


# BASKET
class Basket(models.Model):
    """
    The Basket models
    The items read-to-ship could be linked to it
    And it is linked to a Promo
    """

    promo = models.ForeignKey(Promo, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    final_price = models.DecimalField('Price', max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = 'Basket'
        verbose_name_plural = 'Baskets'
        ordering = ['user']


# BASKITEM
class BasketItem(models.Model):
    """
    The Basket Item model
    wich is linked to a Basket and any item
    is linked to
    """

    ITEM_BOOK = 'b'
    ITEM_MAGAZINE = 'm'

    ITEM_CHOICES = [
        (ITEM_BOOK, 'book'),
        (ITEM_MAGAZINE, 'magazine')
    ]

    item_pk = models.PositiveBigIntegerField('Item ID', null=False)
    # "Book" or "Magazine"?
    item_type = models.CharField(
        'Type', max_length=1, choices=ITEM_CHOICES, default=ITEM_BOOK, blank=True)
    basket = models.ForeignKey(Basket, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'BItem'
        verbose_name_plural = 'BItems'
