from django.db import models

from django.db import models

from boards.models import Board
from users.models import User


class Article(models.Model):
    use_in_migrations = True
    title = models.CharField(max_length=20)
    content = models.TextField()
    writtenDate = models.DateField()
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    boardName = models.ForeignKey(Board, on_delete=models.CASCADE)

    class Meta:
        db_table = "articles"

    def __str__(self):
        return f'{self.pk} {self.title}'
