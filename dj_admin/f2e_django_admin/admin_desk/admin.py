from django.contrib import admin
from admin_desk.models import Favorite, Node, Notification, Plane, Reply, Topic, Transaction, User

#class NodeAdmin(admin.ModelAdmin):
#    fieldsets = [
#            (None, {'fields': ['name', 'slug', 'introduction']}),
#            (None, {'fields': ['plane_id']}),
#            ]
# Register your models here.
admin.site.register(Favorite)
admin.site.register(Node)
admin.site.register(Notification)
admin.site.register(Plane)
admin.site.register(Reply)
admin.site.register(Topic)
admin.site.register(Transaction)
#admin.site.register(User)
