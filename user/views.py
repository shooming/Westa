import json

from django.http        import HttpResponse, JsonResponse
from django.views       import View

from .models            import User


class UserView(View):
    def post(self, request):
        data = json.loads(request.body)
        try:
            if User.objects.filter(user_id = data['id']).exists():
                return JsonResponse({'message':'User already registered'}, status=401)

            if data['id'] == '' or data['password'] == '' or data['eamil'] == '':
                return HttpResponse(status = 400)

            User(
                user_id     = data['id'],
                password    = data['password'],
                email       = data['email']
            )
        except KeyError:
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
