from django.db import models
from django.utils import timezone
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
@receiver(post_save, sender = User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user = instance)

@receiver(post_save, sender = User)
def  save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Recipie_Type(models.Model):
    recipie_name = models.CharField(max_length=60)

    def __str__(self):
        return self.recipie_name

class categories(models.Model):
    category_name = models.CharField(max_length=60)
    
    def __str__(self):
        return self.category_name

class sub_categories(models.Model):
    subcategory_name = models.CharField(max_length=60)
                                                                     
    def __str__(self):
        return self.subcategory_name

class recipie_subtype(models.Model):
    recipie_subtypename = models.CharField(max_length=60)

    def __str__(self):
        return self.recipie_subtypename

class recipies(models.Model):
    recipie_name = models.ForeignKey(recipie_subtype)
    ingredients = models.CharField(max_length=1000)
    preparation = models.CharField(max_length=1000)
    
    def __str__(self):
        return str(self.recipie_name)

class categories_sub_categories_map(models.Model):
    category_id = models.ForeignKey(categories)
    subcategory_id =models.ForeignKey(sub_categories)
    def __str__(self):
        return "{0}-{1}".format(str(self.category_id),str(self.subcategory_id))

class Recipie_Recipie_subtype_map(models.Model):
     Recipietype_id = models.ForeignKey(Recipie_Type)
     Rsubtype_id = models.ForeignKey(recipie_subtype)
     def __str__(self):
        return "{0}-{1}".format(str(self.Recipietype_id),str(self.Rsubtype_id))
        
class Recipies_Rmap_Cmap(models.Model):
    Recipie_id = models.ForeignKey(Recipie_Type)
    Rmap_id = models.ForeignKey(Recipie_Recipie_subtype_map)
    Cmap_id =models.ForeignKey(categories_sub_categories_map,default=1) 
    def __str__(self):
        return "{0}-{1}-{2}".format(str(self.Recipie_id),str(self.Rmap_id),str(self.Cmap_id))    
