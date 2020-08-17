from django.shortcuts import render
from mooproj.models import Cow
from mooproj.forms import TextForm
import subprocess

def index(request):
    if request.method == 'POST':
        form = TextForm(request.POST)
        if form.is_valid():
            new_cow = form.save()
            output = subprocess.run(['cowsay', new_cow.text], capture_output=True, text=True)
            output = output.stdout
            return render(request, 'index.html', {'form': form, 'output': output})
    else:
        form = TextForm()
    return render(request, 'index.html', {'form': form})

def previous_cows(request):
    last_ten = Cow.objects.all().order_by('-id')[:10]
    previous_cows = []
    for cow in last_ten:
        output = subprocess.run(['cowsay', cow.text], capture_output=True, text=True)
        previous_cows.append(output.stdout)
    return render(request, 'previous_cows.html', {'previous_cows': previous_cows})