# Create your views here.
from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import status
from softdesk.models import Contributor, Project,Issue,Comment
from authentication.models import User
from softdesk.serializers import ProjectSerializer, UserSerializer, ContributorSerializer,IssueSerializer,CommentSerializer


class ProjectViewset(viewsets.ModelViewSet):

    serializer_class = ProjectSerializer
    queryset = Project.objects.all()
    lookup_field = "pk"

    def perform_create(self, serializer):
        project_instance = serializer.save()
        Contributor.objects.create(
            project=project_instance, user=self.request.user, role="AU")

    def list(self, request):
        queryset = Project.objects.filter(contributor__user=request.user)
        serializer = ProjectSerializer(queryset, many=True)
        return Response(serializer.data)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def update(self, request, pk=None, *args, **kwargs):
        user = request.user
        instance = self.get_object()
        data = {
            "title": request.POST.get('title', None),
            "description": request.POST.get('description', None),
            "type": request.POST.get('type', None),
        }
        serializer = self.serializer_class(instance=instance, data=data, context={
                                           'author': user}, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class UserViewset(viewsets.ModelViewSet):

    serializer_class = UserSerializer
    queryset = User.objects.all()
    lookup_field = "pk"


class ProjectUserViewset(viewsets.ModelViewSet):
    serializer_class = ContributorSerializer

    def get_queryset(self, *args, **kwargs):
        project = get_object_or_404(Project, id=self.kwargs.get('project_pk'))
        return Contributor.objects.filter(project=project)

    def perform_create(self, serializer, *args, **kwargs):
        project = get_object_or_404(Project, id=self.kwargs.get('project_pk'))
        serializer.save(project=project)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class IssueViewset(viewsets.ModelViewSet):
    serializer_class = IssueSerializer

    def get_queryset(self,*args,**kwargs):
        project = get_object_or_404(Project, id=self.kwargs.get('project_pk'))
        return Issue.objects.filter(project=project)

    def perform_create(self, serializer, *args,**kwargs):
        project = get_object_or_404(Project, id=self.kwargs.get('project_pk'))
        serializer.save(project=project, author= self.request.user)


class CommentViewset(viewsets.ModelViewSet):
    serializer_class = CommentSerializer

    def get_queryset(self,*args,**kwargs):
        issue = get_object_or_404(Issue, id=self.kwargs.get('issue_pk'))
        return Comment.objects.filter(issue=issue)

    def perform_create(self, seriarializer, *args, **kwargs):
        issue = get_object_or_404(Issue, id=self.kwargs.get('issue_pk'))
        seriarializer.save(issue= issue, author=self.request.user)