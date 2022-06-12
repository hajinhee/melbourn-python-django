from django.db import models


class Board(models.Model):
    use_in_migrations = True
    board_id = models.AutoField(primary_key=True)
    board_name = models.CharField(max_length=10)
    create_date = models.DateField()

    class Meta:
        db_table = "boards"

    def __str__(self):
        return f'{self.pk} {self.board_name}'
