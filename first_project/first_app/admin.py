from django.contrib import admin
from first_app.models import Accessrecord,Topic,Webpage,User,UserProfileInfo

# Register your models here.

admin.site.register(Accessrecord)
admin.site.register(Topic)
admin.site.register(Webpage)
admin.site.register(User)
admin.site.register(UserProfileInfo)