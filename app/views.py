from django.shortcuts import render
from urllib3 import request
from app.models import Banner, AboutUsImage, TrustedPartner, Service, News,Testimonials

# Create your views here.


def home(request):
    banner=Banner.objects.last()
    testimonials=Testimonials.objects.order_by('-id')
    service = Service.objects.all()[:10]
    context={
        'banner': banner,
        'testimonials': testimonials,
        'services': service
    }
    return render(request, 'home.html', context)

def about(request):
    about = AboutUsImage.objects.last()
    team = TrustedPartner.objects.all()
    context={
        'about': about,
        'team': team
    }
    return render(request, 'about.html',context)

def services(request):
    services = Service.objects.all()
    context={
        'services': services
    }
    return render(request, 'services.html',context)

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



