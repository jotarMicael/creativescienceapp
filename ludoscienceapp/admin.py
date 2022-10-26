from django.contrib import admin
from ludoscienceapp.models.role import Role
from ludoscienceapp.models.user import User
from ludoscienceapp.models.proyect import Proyect
from ludoscienceapp.models.game_element import GameElement
from ludoscienceapp.models.badge import Badge
from ludoscienceapp.models.token import Token
from ludoscienceapp.models.area import Area
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display=('id','complete_name','username','email','password','profile_image','verified','role_id')
    readonly_fields= ('id',)
class RoleAdmin(admin.ModelAdmin):
    list_display=('id','name')

class ProyectAdmin(admin.ModelAdmin):
    list_display=('id','name','description','image')
    
class TokenAdmin(admin.ModelAdmin):
    list_display=('user_id','token')

class GameElementAdmin(admin.ModelAdmin):
    list_display=('name','area','time_restriction','goal','owner')

class BadgeAdmin(admin.ModelAdmin):
    list_display=('image','parent')

class AreaAdmin(admin.ModelAdmin):
    list_display=('lat','long')

admin.site.register(Role,RoleAdmin)
admin.site.register(User,UserAdmin)
admin.site.register(Token,TokenAdmin)
admin.site.register(Proyect,ProyectAdmin)
admin.site.register(GameElement,GameElementAdmin)
admin.site.register(Badge,BadgeAdmin)
admin.site.register(Area,AreaAdmin)