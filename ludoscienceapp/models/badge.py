
from django.db import models
from creativescienceapp.models.game_element import GameElement
# Create your models here.
class Badge(GameElement):
    image=models.ImageField(upload_to='creativescience/creativescienceapp/static/game_elements_image/',default='creativescience/creativescienceapp/static/game_elements_image/ge.jpg',null=False,blank=False)
    parent=models.ForeignKey('self',null=True,blank=True,on_delete=models.DO_NOTHING)
    class Meta:
        verbose_name='Badge'
        verbose_name_plural="Badges"
        db_table='badge'
    def __str__(self):
        return f'{self.image},{self.parent}'