from django.shortcuts import render


# Create your views here.
def platform(request):
    return render(request, 'fourth_task/platform.html')

def games(request):
    games = ["Atomic Heart", "Cyberpunk 2077"]
    return render(request, 'fourth_task/games.html', {'games': games})

def cart(request):
    return render(request, 'fourth_task/cart.html')



