from django.urls    import path

from .views         import UserView, UserLogin

urlpatterns=[
        path('',UserView.as_view()),
        path('/login',UserLogin.as_view()),
]
