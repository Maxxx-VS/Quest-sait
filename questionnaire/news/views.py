from django.shortcuts import render

def news_home(reques):
    return render(reques, 'main/about.html')
