import datetime
from django.shortcuts import render
from django.utils.timezone import make_aware

from polls.models import News


def index(request):
    news = News.objects.all()
    first = News.objects.first()
    date = datetime.datetime(2025, 1, 2)
    news_in_2024 = News.objects.filter(created_at__lte=make_aware(date))
    context = {'news': news, 'first': first, 'news_in_2024': news_in_2024}
    return render(request, 'index.html', context)
