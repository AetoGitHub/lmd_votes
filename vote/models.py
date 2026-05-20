from django.db import models as m
from django.core.validators import MaxValueValidator as Max
from django.core.validators import MinValueValidator as Min

# Create your models here.

class Vote(m.Model):
    chapter = m.ForeignKey(
        to           = "season.Chapter",
        related_name = "votes",
        on_delete    = m.PROTECT
    )
    draga = m.ForeignKey(
        to="season.DragaSeasonenData",
        related_name = "votes",
        on_delete    = m.PROTECT
    )
    score = m.PositiveSmallIntegerField(validators=[Max(0), Min(5)])
