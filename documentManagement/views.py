from django.shortcuts import render
from base.models import Departement
from .forms import DocumentForm
from .models import Document
from django.shortcuts import redirect
from django.contrib import messages
from .filter import DocumentFilter
from django.http import HttpResponse, JsonResponse
import urllib
from django.contrib.auth.decorators import login_required
from base.decorators import allowedUsers



# Create your views here.
@login_required(login_url= 'userLogin')
def home(request):
    departements = Departement.objects.all()
    documents = Document.objects.all()
    filter = DocumentFilter(request.GET, queryset=documents)
    context = {'departements' : departements ,  'documents':documents , 'filter':filter}
    return render( request, 'documentManagement/home.html', context )
@login_required(login_url= 'userLogin')
@allowedUsers('admins')
def documentRegistration(request) :
    documentForm= DocumentForm()
    print (request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest')  # pakek gini soalnya kita ga pake x-requested-with
    if request.method == "POST":
    #if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
        documentForm = DocumentForm(request.POST, request.FILES)
        if documentForm.is_valid():
            #disini masih ada bug dimana reviewer dan aprover mesti terisi diawal, walaupun niatnya mereka bisa kosong
            doc = documentForm.save(commit=False)
            doc.owner = request.user
            doc.clean()
            doc.save()
            documentForm.save_m2m()
            doc.distribution.add(request.user.position.departement)
            return redirect('DMS')
        else:
            print(str(documentForm.errors) + 'hello ini erronya')
            messages.error(request,'registration error')
    context ={'documentForm':documentForm,}
    return render(request, 'documentManagement/documentForm.html', context)
@login_required(login_url= 'userLogin')
@allowedUsers('admins')
def documentEdit(request,pk) :# how can i made if user update, file existing otomatis terdelete (kalo sekarang kesimpen)
    document  = Document.objects.get(id=pk)
    documentForm = DocumentForm(instance=document)
    #apakah harus ada check disini bahwa request.user.position.departement == document.owner.position.departement ?
    if request.method == 'POST':
        documentForm= DocumentForm(request.POST, request.FILES,instance=document)
        if documentForm.is_valid():
            documentForm.save()
            return redirect('DMS')
        else:
            messages.error(request,'registration eror ')
    context ={'documentForm':documentForm,}

    return render(request, 'documentManagement/documentForm.html', context)
@login_required(login_url= 'userLogin')
@allowedUsers('admins')
def deleteDocument(request, pk) :
    if request.method =="POST":
        document = Document.objects.get(id=pk)
        document.delete()
        return redirect('DMS')

@login_required(login_url='userLogin')
@allowedUsers('admins')
def updateDistribution(request,pk):
    if request.method == "POST":
        document = Document.objects.get(id=pk)
        if not document.is_distributed :
            document.is_distributed = True
        else :
            document.is_distributed = False
        document.save()
        return redirect('DMS')
@login_required(login_url= 'userLogin')
@allowedUsers('admins', 'staff')
def viewDocument(request,pk ):
    document = Document.objects.get(id=pk)
    amazon_url = document.pdf_file.url
    with urllib.request.urlopen(amazon_url) as pdf:
        pdf_data = pdf.read()
    response = HttpResponse(pdf_data, content_type='application/pdf')
    return response

