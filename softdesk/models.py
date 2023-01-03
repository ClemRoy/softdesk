
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings

# Create your models here.


class Project(models.Model):

    class Projecttype(models.TextChoices):
        BACKEND = 'BE', _('Back-end')
        FRONTEND = 'FE', _('Front-end')
        IOS = "IO", _('iOS')
        ANDROID = 'An', _('Android')

    title = models.fields.CharField(max_length=140)
    description = models.fields.CharField(max_length=5000)
    type = models.fields.CharField(choices=Projecttype.choices, max_length=2)
    contributors = models.ManyToManyField(settings.AUTH_USER_MODEL, through="Contributor")
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Contributor(models.Model):

    class Contributortype(models.TextChoices):
        AUTHOR = "AU", _('Author')
        CONTRIBUTOR = "CO", _('Contributor')

    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    role = models.fields.CharField(
        choices=Contributortype.choices, max_length=2)
    created_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('project', 'user')


class Issue(models.Model):

    class Tag(models.TextChoices):
        BUG = 'BU', _('Bug')
        TASK = 'TA', _('Task')
        IMPROVEMENT = 'IM', _('Improvement')

    class Priority(models.TextChoices):
        HIGH = 'HI', _('High')
        MEDIUM = 'ME', _('Medium')
        LOW = 'LO', _('LOW')

    class Status(models.TextChoices):
        IN_PROGRESS = "IP", _('In progress')
        FINISHED = 'FI', _('Finished')

    title = models.fields.CharField(max_length=140)
    description = models.fields.CharField(max_length=5000)
    tag = models.fields.CharField(choices=Tag.choices, max_length=2)
    priority = models.fields.CharField(choices=Priority.choices, max_length=2)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    status = models.fields.CharField(choices=Status.choices, max_length=2)
    createtd_time = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="Issue_author")
    assigned_user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="Assigned_user", null=True)


class Comment(models.Model):
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    description = models.fields.CharField(max_length=5000)
    createtd_time = models.DateTimeField(auto_now_add=True)
