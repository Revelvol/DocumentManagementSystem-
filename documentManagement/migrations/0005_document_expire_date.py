# Generated by Django 4.1.3 on 2022-12-12 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documentManagement', '0004_document_is_distributed_document_validity_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='expire_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]