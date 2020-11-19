from django.shortcuts import render, redirect
from .models import Entry
from .forms import EntryForm

# Create your views here.

def home(request):
    entries = Entry.objects.all()

    context= {
    'entries': entries
    }
    
    return render( request, 'home.html',  context)


def add(request):
    form = EntryForm()

    if request.method =='POST':
        form = EntryForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    

    context = {'form': form}
    
    return render( request, 'add.html', context)

def delete(request, Entry_name):
    Entry.objects.get(text=Entry_name).delete()

        
    
    return redirect('home')
