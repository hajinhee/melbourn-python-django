from django.db import models


class Board(models.Model):
    use_in_migrations = True
    boardName = models.CharField(primary_key=True, max_length=10)
    createDate = models.DateField()

    class Meta:
        db_table = "boards"

    def __str__(self):
        return f'{self.pk} {self.boardName}'
