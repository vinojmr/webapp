from django.shortcuts import render, redirect

from .forms import Celebform
from .models import Celeb
from sample_app2.models import Actor


# Create your views here.
def sample(req):
    celeb = Celeb.objects.filter(name='Messi')
    actor = Actor.objects.filter(name="Mammooty")
    return render(req, 'sample.html', {'celeb': celeb, 'actor': actor})


def celebrity(req):
    celebs = Celeb.objects.all()
    return render(req, 'celeb.html', {'celeb': celebs})


def details(req, id):
    celebs = Celeb.objects.get(id=id)
    return render(req, 'details.html', {'celebs': celebs})


def add(req):
    if req.method == 'POST':
        names = req.POST.get('name', )
        ages = req.POST.get('age', )
        info = req.POST.get('info', )
        images = req.FILES['image']
        celeb = Celeb(name=names, age=ages, info=info, image=images)
        celeb.save()
    return render(req, 'add.html')


def update(req, id):
    celeb = Celeb.objects.get(id=id)
    form = Celebform(req.POST or None, req.FILES, instance=celeb)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(req, 'update.html', {'form': form})


def delete(req, id):
    if req.method == 'POST':
        celeb = Celeb.objects.get(id=id)
        celeb.delete()
        return render(req, 'delete.html')
