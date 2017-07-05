from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key = True)
    username = models.CharField(max_length=50)
    phone_no = models.IntegerField()

    def __str__(self):
        return self.username

class Recipie_Type(models.Model):
    recipie_name = models.CharField(max_length=60)

    def __str__(self):
        return self.recipie_name

class categories(models.Model):
    category_name = models.CharField(max_length=60)
    
    def __str__(self):
        return self.category_name

class sub_categories(models.Model):
    sub_categorie_name = models.CharField(max_length=60)
    
    def __str__(self):
        return self.sub_categorie_name

class recipie_subtype(models.Model):
    recipie_subtype_name = models.CharField(max_length=60)

    def __str__(self):
        return self.recipie_subtype_name

class recipies(models.Model):
    recipie_name = models.CharField(max_length=60)
    ingredients = models.CharField(max_length=1000)
    preparation = models.CharField(max_length=1000)
    
    def __str__(self):
        return self.recipies
class categories_sub_categories_map(models.Model):
    category_id = models.ForeignKey(categories)
    sub_category_id =models.ForeignKey(sub_categories)
    def __str__(Self):
        return self.categories_id
class Recipie_Recipie_subtype_map(models.Model):
     Recipietype_id = models.ForeignKey(Recipie_Type)
     R_subtype_id = models.ForeignKey(recipie_subtype)
     def __str__(self):
        return self.Recipietype_id
        
class Recipies_Rmap_Cmap(models.Model):
    Recipie_id = models.ForeignKey(recipies)
    R_map_id = models.ForeignKey(Recipie_Recipie_subtype_map)
    C_map_id =models.ForeignKey(categories_sub_categories_map,default=1)

    def __str__(Self):
        return self.Recipie_id



  
    
