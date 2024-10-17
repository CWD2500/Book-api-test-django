from django.urls import path
from .  import views

urlpatterns = [
    path('book/' , views.get_all_book , name='book'),
    path('book/<str:pk>/' , views.search_product_book_id ,name ='search_book'),
    path('create/' , views.new_product , name='create_book'),
    path('update/<str:pk>/'   , views.update_product_book  , name="update"),
    path('delete/<str:pk>/'   , views.delete_product_book  , name="delete"),
]
