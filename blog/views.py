from django.shortcuts import render, get_object_or_404
from .models import Article


def landing(request):

    return render(
        request,
        'landing.html',
        {
            'total_articles': Article.objects.count()
        }
    )


def home(request):

    search = request.GET.get('search')

    if search:
        articles = Article.objects.filter(
            title__icontains=search
        )
    else:
        articles = Article.objects.all().order_by('-created_at')

    return render(
        request,
        'home.html',
        {
            'articles': articles,
            'total_articles': Article.objects.count()
        }
    )


def detail(request, id):

    article = get_object_or_404(Article, id=id)

    return render(
        request,
        'detail.html',
        {
            'article': article
        }
    )


def about(request):

    return render(request, 'about.html')