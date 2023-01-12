# Generated by Django 4.1.3 on 2022-12-06 02:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_remove_user_position_user_position'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='departement',
            options={'ordering': ['-name']},
        ),
        migrations.AlterModelOptions(
            name='position',
            options={'ordering': ['-name']},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ['-name']},
        ),
        migrations.AlterField(
            model_name='user',
            name='manager',
            field=models.ForeignKey(blank=True, default='not assigned', null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=200, null=True, unique=True),
        ),
    ]