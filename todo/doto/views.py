from django.shortcuts import render
from django.views.generic import CreateView,ListView,DetailView,DeleteView,UpdateView
from doto.models import todolist
from django.urls import reverse_lazy,reverse
from django.shortcuts import redirect
# Create your views here.
class listitems(ListView):
    model=todolist
    template_name='list_items.html'

# class deleteitem(DeleteView):
#     model=todolist
#     template_name='item_delete.html'
#     success_url=reverse_lazy('all')


class updateitem(UpdateView):
    model=todolist
    fields=('item',)
    template_name='item_update.html'


def deleteitem(request,pk):
    todolist.objects.get(pk=pk).delete()
    return redirect('all')

def crossitem(request,pk):
    item=todolist.objects.get(pk=pk)
    if item.cross:
        item.cross=False
    else:
        item.cross=True
    item.save()
    return redirect('all')

def createitem(request):
    text=request.POST.get('itemtext')
    if len(text)>0:
        todolist.objects.create(item=text)
    return redirect('all')
