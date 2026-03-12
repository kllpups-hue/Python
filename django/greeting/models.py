from django.db import models

class User(models.Model):
    """
    Модель для хранения имен пользователей
    """
    name = models.CharField(
        max_length=100,
        verbose_name='Имя пользователя',
        help_text='Введите ваше имя'
    )
    
    # Добавим дату создания для информации
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания'
    )

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ['-created_at']

    def __str__(self):
        return self.name