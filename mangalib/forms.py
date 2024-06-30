from django import forms
from .models import Book, Author

"""
    CharField
"""

"""class SomeForm(forms.Form):
    username = forms.CharField(label= "Nom d'utilisateur",
                               max_length= 25, 
                               required = True)
    password = forms.CharField(label = "Mot de passe", widget=forms.PasswordInput)
    bio = forms.CharField(label = "Biographie", widget = forms.Textarea)
    publicate = forms.CharField(label = "Publier le contenu ?", widget=forms.CheckboxInput)
    
    languages = [('c', 'Langage C'), ('php', 'Langage PHP')]
    language = forms.MultipleChoiceField(label = "Langages connus", widget = forms.CheckboxSelectMultiple, choices = languages)
    
    colors = [('1', 'Bleu'), ('2', "Jaune"), ('3', 'Rouge'), ('4', 'Vert')]
    color = forms.ChoiceField(label = "Couleur dominante", choices = colors, widget = forms.RadioSelect)
    
    countries = [("1", 'Cameroun'), ("2", "Congo")]
    country = forms.ChoiceField(label = "Pays", choices = countries)"""
    
class BookForm(forms.ModelForm):
    author = forms.ModelChoiceField(queryset= Author.objects.all(), label="Auteur")
    
    class Meta:
        model = Book
        fields = ['title', 'author', 'quantity']
        labels = {'title': 'Titre', 'quantity': 'Quantité'}
        
    def clean_quantity(self):
        quantity = self.cleaned_data['quantity']
        
        if quantity <= 0 or quantity > 100:
            raise forms.ValidationError("La quantité du livre doit etre comprise entre 1 et 100")
        
        return quantity
    
    def clean(self):
        title = self.cleaned_data.get('title')
        quantity = self.cleaned_data.get('quantity')
        
        if title and quantity:
            if title.startswith('Dragon Ball') and quantity < 10:
                raise forms.ValidationError("Minimum une quantité de 10 pour un livre Dragon Ball")

        return self.cleaned_data