# Generated by Django 4.1.3 on 2022-12-11 08:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_alter_departement_options_alter_position_options_and_more'),
        ('documentManagement', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.departement'),
        ),
    ]
