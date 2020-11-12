from rest_framework import routers
from notes import views as myapp_views

router = routers.DefaultRouter()
router.register(r'notes', myapp_views.NoteViewSet)