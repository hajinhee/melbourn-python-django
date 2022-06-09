from django.db import models


class User(models.Model):
    use_in_mygrations = True
    username = models.CharField(primary_key=True, max_length=10)
    password = models.CharField(max_length=10)
    name = models.CharField
    email = models.CharField
    regDate = models.CharField

    class Meta:
        db_table = "users"

    def __str__(self):
        return f'{self.pk} {self.username}'
