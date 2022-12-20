from django.contrib import admin
from authentication.models import User
from softdesk.models import Project, Contributor, Issue, Comment
# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = ['email','id']
    class Meta:
        model = User

class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title','id','description']
    class Meta:
        model = Project

admin.site.register(User, UserAdmin)
admin.site.register(Project,ProjectAdmin)
admin.site.register(Contributor)
admin.site.register(Issue)
admin.site.register(Comment)
