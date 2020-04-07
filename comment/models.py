from django.db import models

class Comment(models.Model):
    user_id     = models.CharField(max_length = 50)
    comment     = models.TextField(max_length = 1000)
    created_at  = models.DateTimeField(auto_now_add = True)
    updated_at  = models.DateTimeField(auto_now = True)

    class Meta:
        db_table = 'comments'
