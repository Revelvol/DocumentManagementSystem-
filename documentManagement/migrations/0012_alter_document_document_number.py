# Generated by Django 4.1.3 on 2022-12-13 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documentManagement', '0011_remove_document_mr_document_approver'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='document_number',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]