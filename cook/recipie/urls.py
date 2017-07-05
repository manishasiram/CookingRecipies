from django.conf.urls import url
from recipie import views

urlpatterns = [url(r'^$',views.index,name='home'),
url(r'recipienames/$',views.recipienames,name='recipienames'),
url(r'categoriestype/$',views.categoriestype,name='categoriestype'),
url(r'rsubtype/$',views.rsubtype,name='rsubtype'),
url(r'scategories/$',views.scategories,name='scategories'),
url(r'rpreparation/$',views.rpreparation,name='rpreparation'),
url(r'categoriesmap/$',views.categoriesmap,name='categoriesmap'),
url(r'recipiemap/$',views.recipiemap,name='recipiemap'),
url(r'rcmap/$',views.rcmap,name='rcmap'),
]

