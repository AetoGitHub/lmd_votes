from django.db import models as m

# Create your models here.

class Season(m.Model):
    name = m.CharField(max_length=100)
    image_url = m.URLField(blank=True)

class Chapter(m.Model):
    number = m.PositiveSmallIntegerField()
    season = m.ForeignKey(
        to           = Season,
        related_name = "chapters",
        on_delete    = m.PROTECT

    )


class DragaSeasonenData(m.Model):
    draga = m.ForeignKey(
        to           = "draga.Feminosa",
        related_name = "data",
        on_delete    = m.PROTECT

    )
    season = m.ForeignKey(
        to           = Season,
        related_name = "data",
        on_delete    = m.PROTECT

    )
    image_url = m.URLField(blank=True)