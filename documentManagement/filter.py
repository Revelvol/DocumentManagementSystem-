import django_filters
from .models import Document
from base.models import Departement


class DocumentFilter(django_filters.FilterSet):
    document_name = django_filters.CharFilter(field_name='document_name',lookup_expr='icontains',
                                              label="Doc Name")
    validity_date = django_filters.DateFilter(field_name='validity_date', lookup_expr='gt' , label ="Valid Date")
    expire_date = django_filters.DateFilter(field_name='expire_date', lookup_expr='gt', label = "Expired Date")
    type = django_filters.CharFilter(field_name='type', lookup_expr='icontains', label="Doc Type")
    doc_number = django_filters.CharFilter(field_name='document_number', lookup_expr='icontains', label="Doc Number")
    departement = django_filters.ModelChoiceFilter(field_name='owner__position__departement', queryset=Departement.objects.all(), label="Departement")
    is_distributed = django_filters.ChoiceFilter(field_name='is_distributed',label='Is Distributed?', choices=( (True, 'Yes'), (False, 'No')))
    class Meta:
        model = Document
        fields = [
            'document_name',
            'type',
            'doc_number',
            'departement',
            'validity_date',
            'expire_date',
            'is_distributed',
        ]