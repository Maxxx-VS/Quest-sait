from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm
from django.views.generic import DetailView, UpdateView, DeleteView

def news_home(request):
    # news = Articles.objects.all() #сортировка новостей
    # news = Articles.objects.order_by('title')[:1]
    news = Articles.objects.order_by('-date')
    return render(request, 'news/news_home.html', {'news': news})

class NewsDetailView(DetailView):
    model = Articles
    template_name = 'news/details_view.html'
    context_object_name = 'article'

class NewsUpdatrlView(UpdateView):
    model = Articles
    template_name = 'news/create.html'
    form_class = ArticlesForm
    #fields = ['title', 'anons', 'full_text', 'date']

class NewsDeleteView(DeleteView):
    model = Articles
    success_url = '/news'
    template_name = 'news/news-delete.html'


def create(request):
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid(): #проверяет корректность заполненых данных
            form.save()
            return redirect('news_home')
        else:
            er = 'Форма была неверной'
    form = ArticlesForm()
    data = {
        'form': form,

    }
    return render(request, "news/create.html", data)