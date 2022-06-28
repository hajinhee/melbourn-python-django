from django.db import models

from boards.models import Board
from users.models import User


class Article(models.Model):
    use_in_migrations = True
    article_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=20)
    content = models.TextField()
    written_date = models.DateField()

    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    board_id = models.ForeignKey(Board, on_delete=models.CASCADE)

    class Meta:
        db_table = "articles"

    def __str__(self):
        return f'{self.pk} {self.title}'
