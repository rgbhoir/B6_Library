from django.shortcuts import redirect, render
from .models import Book
from django.http import HttpResponse
from datetime import datetime #Assignment8
# Create your views here.

#function based/class based views


def homepage(request):  # Any name can be given for arg. we can use req name for arg.    
    name = request.POST.get("bname")
    price = request.POST.get("bprice")
    qty = request.POST.get("bqty")
    ctime = datetime.now()

    if request.method == "POST":        
        if not request.POST.get("bid"):        
            book_name = name
            book_price = price
            book_qty = qty        
                        
            Book.objects.create(name=book_name, price=book_price, qty=book_qty, created_date=ctime, updated_by=101, is_active='Y')
            return redirect("homepage") #made entry in urls.py
        else:
            bid = request.POST.get("bid")
            try:
                book_obj = Book.objects.get(id=bid)
            except Book.DoesNotExist as err_msg:
                print(err_msg)
            book_obj.name = name
            book_obj.price = price
            book_obj.qty = qty
            book_obj.updated_date=ctime
            book_obj.updated_by=101
            book_obj.is_active='Y'

            book_obj.save()
            return redirect("show_all_books")
    elif request.method == "GET":       
        all_books = Book.objects.all()
        data = {"books": all_books}
        return render(request, template_name="home1.html", context=data) 


def show_all_books(request):
    all_books = Book.objects.all()    
    data = {"books":all_books}
    return render(request, "show_books.html", context=data)


def edit_data(request, id):
    book = Book.objects.get(id=id)    
    return render(request, template_name="home1.html", context={"single_book": book}) 

import traceback
def delete_data(request, id):
    print("Delete Data:", request.method)
    if request.method == "POST":
    # if request.method == "GET":  #TEMP for testing the error handling. In address bar type http://127.0.0.1:8000/delete/98765
        try:
            book = Book.objects.get(id=id)
        except Book.DoesNotExist as err_msg:
            traceback.print_exc() # .... book.models.Book.DoesNotExist: Book matching query does not exist.
            print(err_msg) #Book matching query does not exist.
            return HttpResponse(f"Book Does Not Exist for ID:- {id}")
        else:
            book.delete()
        return redirect("show_all_books")
    else:
        return HttpResponse(f"Request method: {request.method} Not Allowed ! Only POST method is allowed")


def activate_book(request, id):  
    if request.method == "POST":  
        try:
            book = Book.objects.get(id=id)
        except Book.DoesNotExist as err_msg:
            traceback.print_exc() # .... book.models.Book.DoesNotExist: Book matching query does not exist.
            print(err_msg) #Book matching query does not exist.
            return HttpResponse(f"Book Does Not Exist for ID:- {id}")
        else:
            book.is_active = 'Y'
            book.updated_date = datetime.now()
            book.updated_by = 102
            book.save()
        return redirect("show_all_books")        
    elif request.method == "GET":         
        all_books = Book.objects.all()
        data = {"books": all_books}
        return render(request, template_name="home1.html", context=data)


def deactivate_book(request, id):  
    if request.method == "POST":  
        try:
            book = Book.objects.get(id=id)
        except Book.DoesNotExist as err_msg:
            traceback.print_exc() # .... book.models.Book.DoesNotExist: Book matching query does not exist.
            print(err_msg) #Book matching query does not exist.
            return HttpResponse(f"Book Does Not Exist for ID:- {id}")
        else:
            book.is_active = 'N'
            book.updated_date = datetime.now()
            book.updated_by = 102
            book.save()
        return redirect("show_all_books")        
    elif request.method == "GET":        
        all_books = Book.objects.all()
        data = {"books": all_books}
        return render(request, template_name="home1.html", context=data)


def activate_all_books(request):  
    if request.method == "POST":  
        try:
            books = Book.objects.all()
        except Book.DoesNotExist as err_msg:
            traceback.print_exc() # .... book.models.Book.DoesNotExist: Book matching query does not exist.
            print(err_msg) #Book matching query does not exist.
            return HttpResponse("Book Does Not Exist")
        else:
            for book in books: 
                book.is_active = 'Y'
                book.updated_date = datetime.now()
                book.updated_by = 102
                book.save()
        return redirect("show_all_books")        
    elif request.method == "GET":        
        all_books = Book.objects.all()
        data = {"books": all_books}
        return render(request, template_name="home1.html", context=data)


def deactivate_all_books(request):  
    if request.method == "POST":  
        try:
            books = Book.objects.all()
        except Book.DoesNotExist as err_msg:
            traceback.print_exc() # .... book.models.Book.DoesNotExist: Book matching query does not exist.
            print(err_msg) #Book matching query does not exist.
            return HttpResponse("Book Does Not Exist")
        else:
            for book in books: 
                book.is_active = 'N'
                book.updated_date = datetime.now()
                book.updated_by = 102
                book.save()
        return redirect("show_all_books")        
    elif request.method == "GET": #WIP Error msg        
        all_books = Book.objects.all()
        data = {"books": all_books}
        return render(request, template_name="home1.html", context=data)



def show_all_active_books(request):
    all_books = Book.objects.all().filter(is_active='Y')    
    data = {"books":all_books}
    return render(request, "show_books.html", context=data)

def show_all_deactive_books(request):
    all_books = Book.objects.all().filter(is_active='N')    
    data = {"books":all_books}
    return render(request, "show_books.html", context=data)


def delete_all_books(request):    
    if request.method == "POST":    
        try:
            # book = Book.objects.get(id=id)
            book = Book.objects.all()
        except Book.DoesNotExist as err_msg:
            traceback.print_exc() # .... book.models.Book.DoesNotExist: Book matching query does not exist.
            print(err_msg) #Book matching query does not exist.
            return HttpResponse("No Book Exist")
        else:
            book.delete()
        return redirect("show_all_books")
    else:
        return HttpResponse(f"Request method: {request.method} Not Allowed ! Only POST method is allowed")


def submit_form(request): #NA
    return HttpResponse("Data in backend")




