# Generated by Django 4.1.3 on 2022-12-12 06:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('documentManagement', '0008_rename_name_document_document_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='mr',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='MR', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='document',
            name='reviewer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='reviewer', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='document',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='owner', to=settings.AUTH_USER_MODEL),
        ),
    ]
