from rest_framework import permissions
from softdesk.models import Project,Contributor,Comment

class isAuthor(permissions.BasePermission):
    message = "this action can only be performed by the author"


    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True

    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True

        if request.method in permissions.SAFE_METHODS:
            return True

        if isinstance(obj,Project):
            try:
                user = Contributor.objects.get(project=obj, user=request.user)
                if user.role == "AU":
                    return True
                else:
                    return False
            except Contributor.DoesNotExist:
                return False
        else:
            if obj.author == request.user:
                return True

        return False

class isContributor(permissions.BasePermission):

    message = "You can't perform this action because you're not a contributor on this project"

    def has_permission(self, request, view):
        iscontributor = False
        try:
            project = Project.objects.get(id=view.kwargs.get("project_pk"))
            if Contributor.objects.filter(project=project,user=request.user).exists():
                iscontributor = True
        except Project.DoesNotExist:
            pass
        if request.user.is_authenticated and iscontributor:
            return True
            


    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True
        if isinstance(obj,Project):
            if Contributor.objects.filter(project=obj,user=request.user).exists():
                return True
        elif isinstance(obj,Comment):
            project = obj.issue.project
            if Contributor.objects.filter(project=project,user=request.user).exists():
                return True
        else:
            if obj.project.contributors.filter(contributor__user=request.user):
                return True
