from django.shortcuts import render,redirect
from .models import Booklist

# Create your views here.
#Fetching all the book data from database
def index(request):
  book=Booklist.objects.all()
  context={
    'books':book
  }
  return render(request,'index.html',context)

#after clicking the edit button it returns a page where all book releted data showed up as it is
def edit(request,id):
  books=Booklist.objects.get(id=id)
  context={
    'book':books
  }
  return render(request,'edit.html',context)

#In edit page you got all the data as it is,you update the books data as you want after hit the update button all the updated books data showed up in the book list/index page
def update(request,id):
  books=Booklist.objects.get(id=id)
  books.title=request.GET['Title']
  books.price=request.GET['Price']
  books.author=request.GET['Author']
  books.save()
  return redirect("/") 


#Delete button delete the book
def delete(request,id):
  books=Booklist.objects.filter(id=id)
  books.delete()
  return redirect('/')

#After clicking the addbook button it returns a page where you can input all the books data in a form
def addbook(request):
  return render(request,'addbook.html') 

#when you clicks the add button you get a page where you can input in a form,and after clicking the add button in current page all of your entry data showed up in the book list
def create(request):
  if request.method=="POST":
    title=request.POST.get("Title")
    price=request.POST.get("Price")
    author=request.POST.get("Author")
    book_data=Booklist(title=title,price=price,author=author)
    book_data.save()
  return redirect("/") 