from django.db import models

class User(models.Model):
    user_id      = models.CharField(max_length = 50)
    password     = models.CharField(max_length = 400)
    email        = models.EmailField(max_length = 200)
    create_at    = models.DateTimeField(auto_now_add = True)
    update_at    = models.DateTimeField(auto_now = True)

    class Meta:
        db_table = 'users'
