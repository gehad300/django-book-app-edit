from django.urls import path
from .views import getallbooks,getonebook,Add_Book,update_Book,delete_book

urlpatterns = [
    path('', getallbooks, name="All_Books"),
    path('<int:book_id>', getonebook, name="book_page"),
    path('create_book',Add_Book,name="Add_Book"),
    path('update_book/<int:book_id>/',update_Book,name="update_Book"),
    path('delete_book/<int:book_id>/',delete_book,name='delete_book')

]
