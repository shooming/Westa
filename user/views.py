import json

from django.http        import HttpResponse, JsonResponse
from django.views       import View

from .models            import User

class UserView(View):
    def post(self, request):
        data = json.loads(request.body)
        User(
                user_id     = data['id'],
                password    = data['password'],
                email       = data['email']
        ).save()

        return HttpResponse(status = 200)

class UserLogin(View):
    def post(self, request):

        data = json.loads(request.body)

        try:

            login_id      = data['id']
            login_pass    = data['password']

            if User.objects.filter(user_id = login_id).exists():
                if login_pass == User.objects.get(user_id = login_id).password:
                    return HttpResponse(status = 200)

            return JsonResponse({'message':'INVALID_USER'}, status = 401)
        
        except KeyError:
            return HttpResponse(status = 400)
