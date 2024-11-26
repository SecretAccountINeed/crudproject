from django.shortcuts import render,get_object_or_404,redirect

from .models import Item


# Create your views here.

# CRUD


# create
def create_item(request):
    if request.method=='POST':
        name=request.POST.get('name')
        description=request.POST.get('description')
        Item.objects.create(name=name,description=description)
        return redirect('item_list')
    return render(request, template_name='item_form.html')
# read
def item_list(request):
    items=Item.objects.all()
    return render(request, template_name='item_list.html', context={'items':items})

# update
def update_item(request,pk):
    item=get_object_or_404(Item,pk=pk)
    if request.method == 'POST':
        item.name=request .POST.get('name')
        item.description=request.POST.get('description')
        item.save()
        return redirect('item_list')
    return render(request,template_name='item_form.html',context={'item':item})

# delete
def delete_item(request,pk):
    item=get_object_or_404(Item,pk=pk)
    if request.method== 'POST':
        Item.delete()
        return redirect('item_list')
    return render(request, template_name='item_confirm_delete.html',context={'item':item})