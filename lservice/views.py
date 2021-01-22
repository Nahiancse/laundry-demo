from django.shortcuts import render,redirect
from .forms import ItemForm
from .models import Item,SubItem

def welcome(request):
   return render(request,'welcome.html')

#
def load_form(request):
    form=ItemForm
    return render(request,"index.html",{'form':form})

#
#
def add(request):
    form=ItemForm(request.POST,request.FILES)
    form.save()
    return redirect('/show')

def show(request):
    item=Item.objects.all
    return render(request,'show.html',{'item':item})

#
# def edit(request,id):
#     service=Item.objects.get(id=id)
#     return render(request,'edit.html',{'service':service})
#
# def update(request, id):
#     service = Item.objects.get(id=id)
#     form=ServiceFome(request.POST, instance=service)
#     form.save()
#     return redirect('/show')
#
#
# def delete(request,id):
#     service = Item.objects.get(id=id)
#     service.delete()
#     return redirect('/show')
#
#
# def search(request):
#     item_name=request.POST['name']
#     service = Item.objects.filter(item__icontains=item_name)
#     return render(request, 'show.html', {'service': service})
