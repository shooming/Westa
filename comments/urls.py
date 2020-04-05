from django.urls    import path

from .views         import UserComment

urlpatterns = [
        path('', UserComment.as_view()),
]
