from django.shortcuts import render , redirect
from .models import MovieVerse
from .forms import MovieVerseForm

# Create your views here.
def movie_anime(request):
    movie_anime = MovieVerse.objects.all()
    
    if request.method == 'POST':
        form = MovieVerseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('movie_anime')

    else:
        form = MovieVerseForm()        

    context = {
        'movie_anime': movie_anime,
        'form': form
    }

    return render(request, 'MovieVerse/movie_verse.html', context)