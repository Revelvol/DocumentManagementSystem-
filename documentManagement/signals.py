from django.dispatch import receiver
from django.db.models.signals import pre_save
from .models import Document
from django.core.exceptions import ValidationError

@receiver(pre_save,sender = Document)
def doc_name_presave(sender,instance, *args, **kwargs):
    if instance.document_number:
        instance.document_number = instance.document_number.lower()
        # query the database :
        if Document.objects.filter(document_number=instance.document_number).exclude(id = instance.id).exists():
            raise ValidationError("document number already exist ")








