# Generated by Django 4.1.3 on 2022-12-04 02:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_alter_position_description_alter_user_manager_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='position',
        ),
        migrations.AddField(
            model_name='user',
            name='position',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.position'),
        ),
    ]
