from django.db import models

class User(models.Model):
    user_id         = models.CharField(max_length = 50)
    user_pass       = models.EmailField(max_length = 200)
    email           = models.CharField(max_length = 50)
    created_at      = models.DateTimeField(auto_now_add = True)
    updated_at      = models.DateTimeField(auto_now = True)

    class Meta:
        db_table = 'users'
