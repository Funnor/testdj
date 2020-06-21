from django.db import models

class Score(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    score = models.IntegerField(default=0)

    class Meta:
        db_table = 't_score'
