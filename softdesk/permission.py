from rest_framework import permissions
from softdesk.models import Project, Contributor, Comment,Issue


def get_pk_or_none(view, *args, **kwargs):
    """Return the pk or None if there is no pk in url"""
    pk = view.kwargs.get("project_pk")
    return pk


class isAuthor(permissions.BasePermission):
    message = "this action can only be performed by the author"

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True

    def has_object_permission(self, request, view, obj):

        if request.method in permissions.SAFE_METHODS:
            return True

        if isinstance(obj, Project):
            try:
                user = Contributor.objects.get(project=obj, user=request.user)
                if user.role == "AU":
                    return True
                else:
                    return False
            except Contributor.DoesNotExist:
                return False
        elif isinstance(obj, Contributor):
            project = obj.project
            try:
                user = Contributor.objects.get(
                    project=project, user=request.user)
                if user.role == "AU":
                    return True
                else:
                    return False
            except Contributor.DoesNotExist:
                return False
        elif isinstance(obj, Issue):
            if obj.author == request.user:
                return True
            else:
                return False
        elif isinstance(obj,Comment):
            if obj.author == request.user:
                return True
            else:
                return False
        else:
            return False
        


class isContributor(permissions.BasePermission):

    message = "You can't perform this action because you're not a contributor on this project"

    def has_permission(self, request, view):
        primary_key = get_pk_or_none(view)
        if primary_key == None:
            return True
        else:
            try:
                project = Project.objects.get(id=primary_key)
                if Contributor.objects.filter(project=project, user=request.user).exists():
                    return True
                else:
                    return False
            except Project.DoesNotExist:
                return False

    def has_object_permission(self, request, view, obj):
        if isinstance(obj, Project):
            if Contributor.objects.filter(project=obj, user=request.user).exists():
                return True
        elif isinstance(obj, Comment):
            project = obj.issue.project
            if Contributor.objects.filter(project=project, user=request.user).exists():
                return True
        else:
            if obj.project.contributors.filter(contributor__user=request.user):
                return True
