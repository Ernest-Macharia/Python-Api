from django.urls import include, path
from . import views

urlpatterns = [
  path('api/notes', views.get_notes),
  #path('addbook', views.add_book),
  #path('updatebook/<int:book_id>', views.update_book),
  #path('deletebook/<int:book_id>', views.delete_book)
]