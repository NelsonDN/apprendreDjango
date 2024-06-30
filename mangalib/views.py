from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.template import loader
# Create your views here.

import datetime
from .models import Book, Author
from .forms import BookForm
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test

def is_visitor(user):
    return user.groups.filter(name = "Visiteur").exists()

"""
    SELECT * : all(), get()

    WHERE : filter() .filter(title = "Naruto")
                __gt, __lt,  gte, __lte, __startswith
    ORDER BY : order_by() -desc
    LIMIT : [:N]

    save(), delete()

    INSERT : create()

    Many-To-Many : * -- * 
         book.authors.add(author)
    
    raw() SQL
    
    
    user.has_perm()
        .all()
        .add()
        .remove()
        .clear()
        .set([])
        
    user.groups.set([gr1, gr2])
    user.groups.add()
    user.groups.remove()
    user.groups.clear()
    
    LoginRequiredMixin
    PermissionRequiredMixin
    
    Django Guardian
    Rules
"""

# settings.LOGNI_URL : /accounts/login

def index(request):
    # context = {"message": "Hello World !",
    #            "numberNews": 15,
    #            "usersList" : ['Tata', 'Toto', 'Titi'],
    #            "publication" : datetime.datetime.now(),
    #            "d1" : datetime.datetime.now(),
    #            "d2" : datetime.datetime.now(),
    #            "text" : "Bonjour et bienvenue sur la bibliotheque de mangas et animes"
    #            }
    context = {
        "books": Book.objects.all()
    }
    
    """if request.method == 'POST':
        form = SomeForm(request.POST)
        
        if form.is_valid():
            return redirect('mangalib:index')
    else:
        form = SomeForm()
    
    context = {"form": form}
    return render(request, "mangalib/index.html", context)"""
    

    return render(request,"mangalib/index.html", context)
    #template = loader.get_template("mangalib/index.html")
    #return HttpResponse(template.render(context, request))

#@login_required
#@permission_required('mangalib.view_book', raise_exception = True)
@user_passes_test(is_visitor)
def show(request, book_id):
    context = {"book": get_object_or_404(Book, pk = book_id)}
    return render(request, "mangalib/show.html", context)    


@permission_required('mangalib.add_book', raise_exception = True)
def add(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect("mangalib:index")
    else:
        form = BookForm()
        
    return render(request,"mangalib/book-form.html", {"form": form})
    
    #author = Author.objects.get(name = "Akira Toriyama")
    
    #book = Book.objects.create(title = "Dragon Ball Z", quantity = 13, author = author)
    
    #book = Book(title = "Dragon Ball Z", quantity = 13, author = author)
    #book.save()

    #return redirect("mangalib:index")

@permission_required('mangalib.change_book', raise_exception = True)
def edit(request, book_id):
    book =  Book.objects.get(pk = book_id)
    
    if request.method == 'POST':
        form = BookForm(request.POST, instance = book)
        
        if form.is_valid():
            form.save()
            return redirect("mangalib:index")
    else:
        form = BookForm(instance = book)
        
    return render(request,"mangalib/book-form.html", {"form": form})    
    #book =  Book.objects.get(title = "Naruto")
    #book.title = "Naruto Shippuden"
    #book.save()

    #return redirect("mangalib:index")

@permission_required('mangalib.delete_book', raise_exception = True)
def remove(request, book_id):
    #book =  Book.objects.filter(title__startswith = "Dragon Ball")
    book =  Book.objects.get(pk = book_id)
    book.delete()

    return redirect("mangalib:index")
 
