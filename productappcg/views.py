from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .forms import MovieForm
from productappcg.models import Movie


# Create your views here.
def index(request):
    movie = Movie.objects.all()
    context = {
        'movie_list': movie
    }
    return render(request, 'index.html', context)


def detail(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    return render(request, 'detail.html', {'movie': movie})
    # return HttpResponse("This is Movie No. %s" %movie_id)


def add_movie(request):
    if request.method == "POST":
        name = request.POST.get('name')
        desc = request.POST.get('desc')
        year = request.POST.get('year')
        img = request.FILES['img']
        movie = Movie(name=name, desc=desc, year=year, img=img)
        movie.save()
        return redirect('/')
    return render(request, 'add.html')


def update_movie(request, id):
    if request.method == 'POST':
        movie = Movie.objects.get(id=id)
        form = MovieForm(request.POST or None, request.FILES, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            print("Form errors:", form.errors)
    else:
        movie = get_object_or_404(Movie, id=id)
        form = MovieForm(instance=movie)
    return render(request, 'update.html', {'form': form, 'movie': movie})

def delete_movie(request, id):
    if request.method == "POST":
        movie = Movie.objects.get(id=id)
        print(movie)
        print('post')
        movie.delete()
        return redirect('/')
    else:
        movie = get_object_or_404(Movie, id=id)
        form = MovieForm(instance=movie)
        print(movie)
        print('get')
    return render(request, 'delete.html',{'form': form, 'movie': movie})
