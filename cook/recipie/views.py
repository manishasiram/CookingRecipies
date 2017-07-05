from django.shortcuts import render,get_list_or_404
from django.utils import timezone
from django.http import HttpResponse
from recipie.models import Recipie_Type 
from django.views.generic import ListView
from recipie.models import categories
from recipie.models import recipie_subtype
from recipie.models import sub_categories
from recipie.models import recipies
from recipie.models import categories_sub_categories_map
from recipie.models import Recipies_Rmap_Cmap
from recipie.models import Recipie_Recipie_subtype_map


# Create your views here.
def index(request):
        return HttpResponse("hello user")
        
def recipienames(request):
    temp = Recipie_Type.objects.all()
    return render(request,'recipie/recipie.html',{'recipienames':temp})

def categoriestype(request):
    temp = categories.objects.all()
    return render(request,'recipie/categories.html',{'categoriestype':temp})

def rsubtype(request):
    temp = recipie_subtype.objects.all()
    return render(request,'recipie/rsubtype.html',{'rsubtype':temp})


def scategories(request):
    temp = sub_categories.objects.all()
    return render(request,'recipie/scategories.html',{'scategories':temp})

def rpreparation(request):
    temp = recipies.objects.all()
    return render(request,'recipie/rpreparation.html',{'rpreparation':temp})
    

def categoriesmap(request):
    temp = categories_sub_categories_map.objects.all()
    return render(request,'recipie/categoriesmap.html',{'categoriesmap':temp})
     

def recipiemap(request):
    temp = Recipie_Recipie_subtype_map.objects.all()
    return render(request,'recipie/recipiemap.html',{'recipiemap':temp})
    

def rcmap(request):
    temp =  Recipies_Rmap_Cmap .objects.all()
    return render(request,'recipie/rcmap.html',{'rcmap':temp})
    
         

         

