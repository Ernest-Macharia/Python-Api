from django.urls import include, path
from .views import NoteCreateApi,NoteListApi,NoteUpdateApi,NoteDeleteApi

urlpatterns = [
  path('api/notes/create', NoteCreateApi.as_view()),
  path('api/notes', NoteListApi.as_view()),
  path('api/notes/create/<int:pk>',NoteUpdateApi.as_view()),
  path('api/notes/create/<int:pk>/delete',NoteDeleteApi.as_view())
  #path('updatebook/<int:book_id>', views.update_book),
  #path('deletebook/<int:book_id>', views.delete_book)
]