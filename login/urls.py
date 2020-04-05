from django.urls    import path

from .views         import LoginCheck

urlpatterns = [
        path('', LoginCheck.as_view()),
]
