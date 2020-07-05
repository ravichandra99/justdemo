from django.contrib import admin

# Register your models here.

from myapp.models import UserMaster,UserInfo,UserType,Company,State,Place
from import_export.admin import ImportExportModelAdmin

@admin.register(UserMaster)
class UserMasterAdmin(ImportExportModelAdmin):
	list_display= ('user', 'full_name', 'usertype', 'company','place','address','email','phone')

@admin.register(UserInfo)
class UserInfoAdmin(ImportExportModelAdmin):
	list_display= ('user', 'invoice', 'total','sold','remaining')


admin.site.register(UserType)
admin.site.register(Company)
admin.site.register(State)
admin.site.register(Place)


admin.site.site_header = 'SuperUser Dashboard'
admin.site.index_title = 'Features Area'                 # default: "Site administration"
admin.site.site_title = 'SuperUser Dashboard'