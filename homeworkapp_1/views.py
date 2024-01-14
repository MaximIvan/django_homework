'''
Задание:

Создайте пару представлений в вашем первом приложении:
— главная
— о себе.

Внутри каждого представления должна быть переменная html — многострочный текст с HTML-вёрсткой и данными о вашем первом Django-сайте и о вас.

Сохраняйте в логи данные о посещении страниц.
'''


from django.shortcuts import render
from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)

def main(request):
    page_main = """
        <div>
            <h1>Главная страница</h1>
            <p>Lorem ipsum is placeholder text commonly used in print, and publishing industries for previewing layouts and visual mockups.</p>
            <ul>
                <li><a href="/main/">главная</a></li>
                <li><a href="/about_me/">О себе</a></li>
            </ul>
            <p>Lorem ipsum is placeholder text commonly used in print</p>
        </div>
        <form action='http://127.0.0.1:8000/about_me/' target="_blank">
            <button>О себе</button>
        </form>
        <br>
        <footer>
            <div>
                <p> Контакты: </p>
            </div>
        </footer>
        """
    logger.info(f'Страница "Главная" успешно открыта')
    return HttpResponse(page_main)

def about_me(request):

    logger.info(f'Страница "О себе" успешно открыта')
    return render(request, 'homeworkapp_1/about_me.html')