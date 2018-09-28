from django.db import models

class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    post_user = models.CharField(max_length=255, null=True, blank=True)
    post_time = models.DateTimeField(null=True, blank=True)
    post_title = models.CharField(max_length=255, null=True, blank=True)
    post_body = models.TextField(null=True, blank=True)
    def __str__(self):
        return self.post_title
