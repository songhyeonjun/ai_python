from django.db import models
from datetime import timezone

# Create your models here.
class Visual(models.Model) :
    place_idx = models.IntegerField(db_column='place_idx', primary_key=True)
    place_info = models.CharField(db_column='place_info', max_length=500)
    place_area = models.CharField(db_column='place_area', max_length=30)
    place_view = models.IntegerField(db_column='place_view')
    place_like = models.IntegerField(db_column='place_like')

    class Meta:
        managed = True
        db_table = 'place1'
