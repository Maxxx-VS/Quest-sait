from django.shortcuts import render
from .models import Articles
from .forms import ArticlesForm

def news_home(request):
    # news = Articles.objects.all() #сортировка новостей
    # news = Articles.objects.order_by('title')[:1]
    news = Articles.objects.order_by('-date')
    return render(request, 'news/news_home.html', {'news': news})

def create(request):
    if request.method == 'POST':

    form = ArticlesForm()
    data = {
        'form': form
    }
    return render(request, "news/create.html", data)