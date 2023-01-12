from django.forms import ModelForm
from .models import Document

class DocumentForm(ModelForm):
    class Meta:
        model = Document
        fields = "__all__"
        exclude = ['owner', 'is_distributed']
