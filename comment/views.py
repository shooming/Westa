import json

from django.http        import HttpResponse, JsonResponse
from django.views       import View

from user.models       import User
from .models           import Comment


class UserComment(View):

    def post(self, request):
        try:
            data = json.loads(request.body)
            
            if User.objects.filter(user_id = data['id']).exists():
                Comment(
                        user_id     = data['id'],
                        comment     = data['comment']
                    ).save()
                return HttpResponse(status = 200)
            return JsonResponse({'message':'INVALID_USER'}, status = 401)
        except KeyError:
            return HttpResponse(status = 400)

    def get(self, requset):
        data = Comment.objects.values()
        return JsonResponse({'comment': list(data)}, status=200)

class ShowComment(View):

    def get(self, request):

        user_name = Comment.objects.values('user_id').distinct()
        
        comment_box = []
        save = []

        for a in user_name:
            key = a['user_id']
            for b in Comment.objects.filter(user_id = key):
                save.append(b.comment)
            comment_box.append((key, save))
            save=[]

        print(comment_box)


        return JsonResponse({'message':comment_box}, status = 200)
