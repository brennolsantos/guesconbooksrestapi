from django.urls import path, include
import store.views as views

app_name = 'store'

urlpatterns = [
    path('book-search', views.SearchBook.as_view(), name='book-search'),
    path('update-book/<int:pk>', views.UpdateBook.as_view(), name='update-book'),
    path('book/<int:pk>', views.RetrieveBook.as_view(), name='book'),
    path('create-book', views.CreateBook.as_view(), name='create-book'),
    path('delete-book/<int:pk>', views.DeleteBook.as_view(), name='delete-book'),
    path('magazine-search', views.SearchMagazine.as_view(), name='magazine-search'),
    path('update-magazine/<int:pk>',
         views.UpdateMagazine.as_view(), name='update-magazine'),
    path('magazine/<int:pk>', views.RetrieveMagazine.as_view(), name='magazine'),
    path('create-magazine', views.CreateMagazine.as_view(), name='create-magazine'),
    path('delete-magazine<int:pk>',
         views.DeleteMagazine.as_view(), name='delete-magazine'),
    path('search-author', views.SearchAuthor.as_view(), name='search-author'),
    path('buy-item', views.buy_item, name='buy-item')
]
