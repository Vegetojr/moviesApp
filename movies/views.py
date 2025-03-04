from django.shortcuts import render, HttpResponse

# Create your views here.


def index(request):
    context = {
        'movies': ['A silent voice', 'josee, the tiger and the fish', 'Maquia']
    }
    return render(request, 'movies/index.html', context)


def about(request):
    return render(request, 'movies/about.html', {'movies': 'A silente voice'})
