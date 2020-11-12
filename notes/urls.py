from django.urls import include, path
from .views import NoteCreateApi,NoteListApi

urlpatterns = [
  path('api/notes', NoteCreateApi.as_view()),
  path('api/note', NoteListApi.as_view()),
  #path('updatebook/<int:book_id>', views.update_book),
  #path('deletebook/<int:book_id>', views.delete_book)
]