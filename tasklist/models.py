from django.db import models


class tasklist(models.Model):
    task_id = models.IntegerField(default=0)
    task_name = models.CharField(max_length=100, default='')
    is_checked = models.BooleanField(default=False)



