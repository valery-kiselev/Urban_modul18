from django.shortcuts import render


# Create your views here.
def platform(request):
    title = 'Главная страница'
    context = {'title': title}
    return render(request, 'platform.html', context)

def games(request):
    title = 'Игры'
    context = {'title': title}
    return render(request, 'games.html', context)

def cart(request):
    title = 'Корзина'
    context = {'title': title}
    return render(request, 'cart.html', context)
