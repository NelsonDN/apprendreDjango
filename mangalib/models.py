from django.db import models

"""
    primary_key
    unique
    default
    null
    blank

    CharField
    IntegerField
    DateField
    DateTimeField
    FloatField
    EmailField
    BooleanField
    EmailField

    Many-To-Many : * -- * 
        field = models.ManyToManyField(ModelA)
    One-To-One : 1 -- 1
        
"""

class Author(models.Model):
    name = models.CharField(max_length=64, unique=True, verbose_name= "Nom")
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Auteur"
        verbose_name_plural = "Auteurs"
        #db_table = ""    #modifier le nom de la table enregistree dans la bd

class Book(models.Model):
    title = models.CharField(max_length=64, unique=True, verbose_name= "Titre")
    quantity = models.IntegerField(default = 1, verbose_name= "Quantité")
    author = models.ForeignKey(Author, on_delete=models.DO_NOTHING, verbose_name= "Auteur")
    
    def __str__(self): 
        return self.title
    
    class Meta:
        verbose_name = "Livre"
        verbose_name_plural = "Livres"
        permissions = [
            ('apply_promo_code', 'Peut appliquer des migrations')
        ]