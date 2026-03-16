from django.shortcuts import render
from urllib3 import request
from app.models import Banner, AboutUsImage, TrustedPartner, Service, News

# Create your views here.


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def management(request):
    return render(request, 'management.html')

def news(request):
    all_news=News.objects.order_by('-id')
    context={
        'news': all_news
    }

    return render(request, 'gallery.html',context)

def news_details(request, id):
    news_item = News.objects.get(id=id)
    context = {
        'news': news_item
    }
    return render(request, 'news_details.html', context)


def contact(request):
    return render(request, 'contact.html')



