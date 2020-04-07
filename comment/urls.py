from django.urls    import path

from .views         import UserComment, ShowComment


urlpatterns = [
        path('', UserComment.as_view()),
        path('/shcomment', ShowComment.as_view()),
]
