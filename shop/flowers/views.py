from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Flower , FlowerTypes


# Create your views here.

def home_view(request):
    ctx = {}
    ctx['all_flowers'] = Flower.objects.all()
    return render(request,"index.html",ctx)

def detail_view(request, pk):
    ctx = {}
    ctx['all_flowers'] = Flower.objects.all()
    ctx['current_flower'] = Flower.objects.get(id=pk)
    return render(request, "flowers/detail_view.html", ctx)

def delete_flower(request, pk):
    ctx = {}
    ctx['all_flowers'] = Flower.objects.all()
    try:
        Flower.objects.get(id=pk).delete()
        ctx['deleted'] = True
    except Exception as e:
        ctx['error'] = e
    return render(request,"index.html",ctx)

def delete_all(request):
    Flower.objects.all().delete()
    return redirect('/')

def create_new(request):
    ctx = {}
    ctx['all_types'] = FlowerTypes.objects.all()
    template_path = "flowers/create_new.html"
    if request.method == 'GET':
        return render(request, template_path, ctx)
    elif request.method == 'POST':
        try:
            Flower.objects.create(
                type_flower=FlowerTypes.objects.get(id=request.POST.get('type_flower')),
                title=request.POST.get('title'),
                price=request.POST.get('price'),
                height=request.POST.get('height')
            )
            ctx['added'] = True
        except Exception as e:
            ctx['error'] = e
        return render(request, template_path, ctx)

