from enum import unique
from django.db import models
from ludoscienceapp.models.user import User
import abc


class AbstractModelMeta(abc.ABCMeta, type(models.Model)):
    pass


class Progress(models.Model, metaclass=AbstractModelMeta):
    user= models.ForeignKey(User,blank=False,null=False,on_delete=models.DO_NOTHING)
    progress=models.FloatField(default=0,blank=False,null=False)
    

    class Meta:
        verbose_name='Progress'
        verbose_name_plural="Progress"
        db_table='progress'
        abstract = True


    def __str__(self):
        return f'{self.user},{self.progress}'     

    
    def increment_progress(self,goal,count):
        if (self.progress<100):
            self.progress=(count / goal)*100    
            self.save()