from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.paginator import Paginator
from .models import *


# Create your views here.

def post_list(request):
    # получаем все посты
    posts = Post.objects.all()

    # создаем пагинатор
    paginator = Paginator(posts, 2)  # 10 постов на странице

    # получаем номер страницы, на которую переходит пользователь
    page_number = request.GET.get('page')

    # получаем посты для текущей страницы
    page_posts = paginator.get_page(page_number)

    # передаем контекст в шаблон
    return render(request, 'post_list.html', {'page_posts': page_posts})


class Platform(TemplateView):
    template_name = 'platform.html'


def Games(request):
    title = 'Игрулечки'
    games = Game.objects.all()
    context = {
        'title': title,
        'games': games,
    }
    return render(request, 'games.html', context, )


def Cart(request):
    title = 'Корзина'
    cart = []
    cart_len=len(cart)
    context = {
        'title': title,
        'cart': cart,
        'cart_len': cart_len,
    }
    return render(request, 'cart.html', context)


from django.http import HttpResponse

# Create your views here.

def sign_up_by_html(request):
    if request.method == 'POST':
        users = Buyer.objects.all()
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')
        info = {}
        context = {
            'info': info
        }
        for user in users:
            if user.username == username:
                info.update({'error': 'Такой пользователь уже существует'})
                return render(request, 'registration_page.html', context)
        if password != repeat_password:
            info.update({'error': 'Пароли не совпадают'})
            return render(request, 'registration_page.html', context)
        if int(age) < 18:
            info.update({'error': 'Вы должны быть старше 18'})
            return render(request, 'registration_page.html', context)
        Buyer.objects.create(username=username, balance=100, age=age)
        return HttpResponse(f'Приветствуем, {username}')

    return render(request, 'registration_page.html')


