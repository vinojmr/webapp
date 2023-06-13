from django.shortcuts import render, redirect
from .models import Actor
from .forms import Actor_form
# Create your views here.


def index(req):
    actor = Actor.objects.all()

    return render(req, 'actors.html', {'actor': actor})


def details2(req, actor_id):
    actor = Actor.objects.get(id=actor_id)
    return render(req, 'details2.html', {'actors': actor})


def add2(req):
    if req.method == 'POST':
        name = req.POST.get('name',)
        age = req.POST.get('age',)
        about = req.POST.get('about',)
        image = req.FILES['image']
        actor = Actor(name=name, age=age, about=about, image=image)
        actor.save()
    return render(req, 'add2.html')


def update2(req, actor_id):
    actor = Actor.objects.get(id=actor_id)
    forms = Actor_form(req.POST or None, req.FILES, instance=actor)
    if forms.is_valid():
        actor.save()
        return redirect('/')
    return render(req, 'update2.html', {'form': forms})
