# Generated by Django 4.1.1 on 2022-12-20 10:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('softdesk', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='assigned_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Assigned_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
