from django.db import models


class User(models.Model):
    use_in_mygrations = True
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=10)
    password = models.CharField(max_length=10)
    name = models.TextField()
    email = models.TextField()
    reg_date = models.DateField()

    class Meta:
        db_table = "users"

    def __str__(self):
        return f'{self.pk} {self.user_name}'

