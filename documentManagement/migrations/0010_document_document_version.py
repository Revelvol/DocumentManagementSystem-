# Generated by Django 4.1.3 on 2022-12-12 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documentManagement', '0009_document_mr_document_reviewer_alter_document_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='document_version',
            field=models.IntegerField(default=0),
        ),
    ]
