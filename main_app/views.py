from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Moment
from .forms import MomentForm, NewForm 


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
  context = { 'moment': found_moment }
  return render(request, 'moments/moments_detail.html', context)

# CREATE MOMENT
def create_moment(request):
  if request.method == 'GET':
    form = MomentForm()
    context = {
      'form': form
    }

    return render(request, 'moment/moments_new.html', context)
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
      moment = moment.save()
      return redirect('detail', moment.id)


# NEW MOMENT
def new_moment(request, moment_id):
  form = NewForm(request.POST)
  if form.is_valid():
    new_moment = form.save(commit=False)
    new_moment.moment_id = moment_id
    new_moment.save()
    return redirect('detail', moment_id)

