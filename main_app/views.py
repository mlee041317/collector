from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Moment
from .forms import MomentForm, ManyForm


# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def reviews(request):
  return render(request, 'reviews.html')


# INDEX MOMENT
def index(request):
  moments = Moment.objects.all()
  context = {'moments': moments }
  return render(request, 'moment/moments_index.html', context)

# DETAIL MOMENT
def detail(request, moment_id):
  found_moment = Moment.objects.get(id=moment_id)
  many_form = ManyForm()
  context = { 
    'moment': found_moment, 
    'many_form': many_form,
  }
  return render(request, 'moment/detail.html', context)

# CREATE MOMENT
def create_moment(request):
  if request.method == 'GET':
    form = MomentForm()
    context = {
      'form': form
    }

    return render(request, 'moment/create_moment.html', context)
  else:
    form = MomentForm(request.POST)
    if form.is_valid():
      moment = form.save()

      return redirect('detail', moment.id)


# DELETE MOMENT
def delete_moment(request, moment_id):
  moment = Moment.objects.get(id=moment_id)
  moment.delete()
  return redirect('index')


# UPDATE MOMENT
def update_moment(request, moment_id):
  moment = Moment.objects.get(id=moment_id)

  if request.method == 'GET':
    form = MomentForm(instance=moment)
    context = {
      'form': form
    }

    return render(request, 'moment/moment_edit.html', context)
  else:
    form = MomentForm(request.POST, instance=moment)
    if form.is_valid():
      moment = form.save()
      return redirect('detail', moment.id)


# FEELING MOMENT
def create_feeling(request, moment_id):
  form = ManyForm(request.POST)
  if form.is_valid():
    many_feeling = form.save(commit=False)
    many_feeling.moment_id = moment_id
    many_feeling.save()
    return redirect('detail', moment_id)
