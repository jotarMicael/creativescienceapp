


from django.db import models
from model_utils.managers import InheritanceManager
from ludoscienceapp.models.user  import User
from ludoscienceapp.models.project_subarea import ProjectSubArea
from ludoscienceapp.models.project import Project
from ludoscienceapp.models.time_restriction import TimeRestriction





class GameElement(models.Model):
    objects = InheritanceManager() 
    name=models.CharField(blank=False,unique=True,null=False,max_length=150)
    goal=models.IntegerField(blank=True,null=True)
    owner=models.ForeignKey(User,null=True,blank=True,on_delete=models.DO_NOTHING)
    rate=models.FloatField(blank=True,null=True)
    project=models.ForeignKey(Project,blank=False,null=False,on_delete=models.DO_NOTHING,related_name='%(class)s')
    area=models.ForeignKey(ProjectSubArea,null=True,blank=True,on_delete=models.DO_NOTHING)
    time_restriction=models.ForeignKey(TimeRestriction,null=True,blank=True,on_delete=models.DO_NOTHING)
    checkin=models.ManyToManyField('ludoscienceapp.checkin', related_name='%(class)s_checkins')
    user_actives=models.ManyToManyField('ludoscienceapp.user', related_name='%(class)s_actives')
    user_completes=models.ManyToManyField('ludoscienceapp.user', related_name='%(class)s_completes')
    public=models.BooleanField(blank=False,null=False,default=1)

    class Meta:
        verbose_name='GameElement'
        verbose_name_plural="GameElements"
        db_table='game_element'



    def __str__(self):
        return f'{self.name},{self.goal},{self.owner},{self.rate},{self.project}'     

    def add_checkin(self,checkin_,user_id):
        if(self.time_restriction.is_valid_time(checkin_.get_date()) and self.area.is_valid_area(checkin_.get_latitude(),checkin_.get_longitude()) and self.is_my_user_active(user_id)):
            self.checkin.add(checkin_)
            self.increment_progress(user_id)

    def get_progress_user(self,user_id_):
 
      progress_ge=self.progress_set.get(user_id=user_id_)
      return progress_ge.progress

    def is_my_user_active(self,user_id):
         return (self.user_actives.filter(id=user_id).exists())
       
    def is_my_user_complete(self,user_id):
         return (self.user_completes.filter(id=user_id).exists())    
           
    def get_id_project(self):
        return self.project.id

    def get_name(self):
        return self.name

    def get_goal(self):
        return self.goal
    
    def get_checkins(self):
        return self.checkin

    def change_state(self):
        if self.public:
            self.public=False
        else:
            self.public=True
        self.save()

    def increment_progress(self,user_id_):
        
        progress=self.progress_set.get(user_id=user_id_)
        progress.increment_progress(self.get_goal(),self.get_checkins().filter(user_id=user_id_).count())

    
    def update(self,name,area,time_restriction,goal):
       self.name=name
       self.area=area
       self.time_restriction=time_restriction
       self.goal=goal
       self.save()
       
    def get_progress_user(self,user_id_):
      progress_ge=self.progress_set.get(user_id=user_id_)
      return progress_ge.progress

    def get_state(self):
        if self.public:
            return 'Restaurado'
        return 'Borrado'