from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages
from .models import User

def index(request):
    """
    Главная страница с формой ввода имени и приветствием
    """
    context = {}
    
    if request.method == 'POST':
        # Получаем имя из формы
        name = request.POST.get('name', '').strip()
        
        # Проверка на пустое имя
        if not name:
            messages.error(request, 'Пожалуйста, введите ваше имя!')
        else:
            try:
                # Сохраняем имя в базу данных
                user = User.objects.create(name=name)
                context['greeting_name'] = name
                messages.success(request, f'Привет, {name}! Рады видеть вас снова!')
            except Exception as e:
                # Обработка ошибок базы данных
                messages.error(request, 'Произошла ошибка при сохранении. Пожалуйста, попробуйте снова.')
    
    return render(request, 'greeting/index.html', context)