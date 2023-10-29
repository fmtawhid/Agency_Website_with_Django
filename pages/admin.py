from django.contrib import admin
from . models import teamList,brandList,reviewList
from . models import contactList, packageList, projectList
# About page model admin here.


class listD(admin.ModelAdmin):
    list_display=('teamImg', 'teamName', 'teamTitle')
    list_filter=('teamName', 'teamTitle')
    list_per_page= (4)
    search_fields = ('teamImg', 'teamName', 'teamTitle' )
admin.site.register(teamList, listD)

class listD(admin.ModelAdmin):
    list_display=('brName', 'brImg')
admin.site.register(brandList, listD)

class listD(admin.ModelAdmin):
    list_display=('bayarName', 'bayarLoct', 'bayarImg', 'bayarDisc')
admin.site.register(reviewList, listD)




# Contact page model admin here.
class rqOffer(admin.ModelAdmin):
    list_display=('help', 'pkg', 'name', 'email', 'massage')

    list_filter=('help', 'pkg')
    list_per_page= (4)
    search_fields = ('help', 'pkg', 'name', 'email', 'massage' )
admin.site.register(contactList, rqOffer)

# package List Admin
admin.site.register(packageList)

# Project Done List Admin added
admin.site.register(projectList)



