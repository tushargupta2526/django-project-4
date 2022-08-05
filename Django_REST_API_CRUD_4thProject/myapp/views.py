from django.shortcuts import redirect, render
from django.urls import is_valid_path
from myapp.form import BookForm
from myapp.models import Book

# Create your views here.
def index(request):

    if request.method=='POST':
        form=BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/show')
            
    else:        
        obj=BookForm() #GET
        return render(request,'BookForm.html',{'book_obj':obj})


def show(request):
    books=Book.objects.all() #select * from books
    return render(request,'show.html',{'all_books':books})

#used to fetch the book record from table(SQL) and display it using edit.html
def edit(request,id):
    book=Book.objects.get(id=id) #fetching individual book details using unique id
    return render(request,'edit.html',{'book':book})


#update the employee details retrieved using edit.html
def update(request,id):
    
    book=Book.objects.get(id=id)
    form=BookForm(request.POST,instance=book)
    if form.is_valid():
        form.save() #saving details in table
        return redirect('/show')

    return render(request,'edit.html',{'book':book})

def delete(request,id):
    book=Book.objects.get(id=id)
    book.delete()
    return redirect('/show')
    











