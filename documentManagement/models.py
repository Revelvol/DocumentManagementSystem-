from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator



# Create your models here.
class Document(models.Model):
    document_name = models.CharField(max_length= 200, null = True, blank=False,)
    document_number = models.CharField (max_length= 200, null = True, blank=True,)
    document_version = models.IntegerField(null = False , blank = False, default=0)
    owner = models.ForeignKey('base.User', on_delete=models.SET_NULL, null=True,related_name= 'owner' )
    DOCUMENT_TYPES = (
        ('Man', 'Manual'),
        ('Proc', 'Procedure'),
        ('Spec', 'Specification'),
        ('Form', 'Form'),
        ('WI', 'Working Instruction'),
    )
    type = models.CharField(max_length= 50, choices= DOCUMENT_TYPES, default= "-------")
    pdf_file = models.FileField(
        validators=[FileExtensionValidator(['pdf'])],
        blank=True
    )
    validity_date = models.DateField( default=timezone.now , null=True, blank=False ) # i think mesti add berdasarkan timezone kalo forma
    expire_date = models.DateField(null=True, blank=True)
    is_distributed = models.BooleanField(default=False)
    distribution = models.ManyToManyField('base.Departement')
    class Meta:
        ordering = [
            'owner'
        ]
    def clean(self):
        if self.expire_date and self.validity_date and self.expire_date <= self.validity_date:
            raise ValidationError('The expire date must be more than the validity date.')
    @property
    def is_valid(self):
        if not self.expire_date :
            return True
        return timezone.now().date() < self.expire_date
    def __str__(self):
        return self.document_number + " || " + self.document_name
