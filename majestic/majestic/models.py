from django.db import models


class Message(models.Model):
    """Model for feedback form"""
    fullname = models.CharField(max_length=256, verbose_name='Полное имя')
    user_phone = models.CharField(max_length=20, verbose_name='Номер телефона')
    user_email = models.CharField(max_length=256, verbose_name='E-mail')
    message = models.TextField(verbose_name='Сообщение')
    date_sent = models.DateTimeField(auto_now_add=True, verbose_name='Дата отправки')
    checked = models.BooleanField(verbose_name='Состояние',
                            help_text='Поставить отметку, если тема закрыта')

    class Meta:
        verbose_name = 'Сообщение/Вопрос'
        verbose_name_plural = 'Сообщения/Вопросы'
        ordering = ['-date_sent', 'fullname']

    def __str__(self):
        return self.fullname