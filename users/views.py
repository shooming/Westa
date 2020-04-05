import  json

from django.http    import HttpResponse, JsonResponse
from django.views   import View
from .models        import User

class UserView(View):

    def post(self, request):
        data = json.loads(request.body)

        User(
            user_id      = data['id'],
            user_pass    = data['password'],
            email        = data['email'],
        ).save()

        return  HttpResponse(stauts = 200)

    def get(self, request):
        user = User.objects.values()

        return JsonResponse({'data':list(user)}, status = 200)
