from django.contrib import admin
from recipie.models import *
admin.site.register(Profile)
admin.site.register(Recipie_Type)
admin.site.register(categories)
admin.site.register(sub_categories)
admin.site.register(recipie_subtype)
admin.site.register(recipies)
admin.site.register(categories_sub_categories_map)
admin.site.register(Recipie_Recipie_subtype_map)
admin.site.register(Recipies_Rmap_Cmap)

# Register your models here.
