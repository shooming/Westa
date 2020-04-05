import json

from django.http      import HttpResponse, JsonResponse
from django.views     import View
from users.models     import User

class LoginCheck(View):

    def post(self, request):

        data = json.loads(request.body)

        name        = data['id']
        password    = data['password']

        check = User.objects.filter(user_id = name, user_pass = password)

        if not check:
            return JsonResponse({'message':'INVALID_USER'}, status = 401)
        elif name == check[0].user_id:
            if password == check[0].user_pass:
                return JsonResponse( {'로그인 결과:' : name +'님 로그인에 성공하셨습니다.'}, status = 200)


    def get(self, request):

        user = User.objects.values()

        return JsonResponse({'data':list(user)}, status = 200)
