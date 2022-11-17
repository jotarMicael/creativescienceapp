from django.contrib import admin
from ludoscienceapp.models.role import Role
from ludoscienceapp.models.user import User
from ludoscienceapp.models.project import Project
from ludoscienceapp.models.badge import Badge


from ludoscienceapp.models.token import Token
from ludoscienceapp.models.check_in import CheckIn
from ludoscienceapp.models.project_subarea import ProjectSubArea
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display=('id','complete_name','username','email','password','profile_image','verified','role_id')
    readonly_fields= ('id',)

class RoleAdmin(admin.ModelAdmin):
    list_display=('id','name')

class ProjectAdmin(admin.ModelAdmin):
    list_display=('id','name','description','image')
    
class TokenAdmin(admin.ModelAdmin):
    list_display=('user_id','token')

class BadgeAdmin(admin.ModelAdmin):
    list_display=('image','parent')

class AreaAdmin(admin.ModelAdmin):
    list_display=('lat','long')

class CheckInAdmin(admin.ModelAdmin):
    list_display=('user','project','latitude','longitude','datetime')

class ChallengeProgressAdmin(admin.ModelAdmin):
    list_display=('user','challenge','progress')

class BadgeProgressAdmin(admin.ModelAdmin):
    list_display=('user','badge','progress')

class SubAreaAdmin(admin.ModelAdmin):
    list_display=('area','sub_area')

admin.site.register(Role,RoleAdmin)
admin.site.register(User,UserAdmin)
admin.site.register(Token,TokenAdmin)
admin.site.register(Project,ProjectAdmin)
admin.site.register(Badge,BadgeAdmin)
admin.site.register(CheckIn,CheckInAdmin)
admin.site.register(ProjectSubArea,SubAreaAdmin)