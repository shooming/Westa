import json

from django.views   import View
from django.http    import HttpResponse, JsonResponse
from .models        import Comment
from users.models   import User

class UserComment(View):

    def post(self, request):

        data = json.loads(request.body)

        user_name    = data['id']
        user_comment = data['comment']

        check = User.objects.filter(user_id = user_name)

        if not check:
            return JsonResponse({'message':'INVALID_USER'}, status = 401)

        elif (not user_name) == False and (not user_comment) == False:
            Comment(
                        user_id = data['id'],
                        comment = data['comment'],
                    ).save()

            return HttpResponse(status = 200)

        else:
            return JsonResponse({'message':'notting data'}, status = 400)

    def get(self, request):

      try:
        data = json.loads(request.body)

        user_name     = data['id']
        comments      = []

        user_check  = User.objects.filter(user_id = user_name)
        select_user = Comment.objects.filter(user_id = user_name)


        if (not select_user) != True and (not user_check) != True:
            for a in list(select_user):
                comments.append(a.comment)
            return JsonResponse({ user_name + '의 코멘트 모음' : comments}, status = 200)

        elif (not user_check) != True:
            return JsonResponse({ user_name :'해당 사용자의 코멘트가 없습니다.'}, status = 200)

        else:
            return JsonResponse({'사용자 아이디 없음' : '사용자 등록 해주세요'}, status = 200)

      except:
            return JsonResponse({'message':'Data Not Exist'}, status = 400)

