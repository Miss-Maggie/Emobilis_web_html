from django.shortcuts import render, redirect, get_object_or_404
from .models import  Item
from .form import  ItemForm

# Create your views here.
# READ(list all items)
def item_list(request):
    items = Item.objects.all()
    return render(request, 'item_list.html', {'items': items})

# CREATE
def item_create(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('item_list')
    else:
       form = ItemForm()
    return render(request,'item_form.html',{'form':form})
# UPDATE
def item_update(request,item_id):
    item = get_object_or_404(Item,id=item_id)
    if request.method == 'POST':
        form = ItemForm(request.POST,instance=item)
        if form.is_valid():
            form.save()
            return redirect('item_list')
    else:
        form = ItemForm(instance=item)
    return render(request,'item_form.html',{'form':form})

# DELETE
def item_delete(request,item_id):
    item = get_object_or_404(Item,id=item_id)
    if request.method == 'POST':
        item.delete()
    return redirect('item_list')
    return render(request,'item_delete.html',{'item':item})