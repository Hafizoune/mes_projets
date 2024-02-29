from django.shortcuts import render
from .models import Article

def home(request):
    list_articles = Article.objects.all()
    context = {"liste_articles":list_articles}
    return render(request, "blog/index.html",context)
