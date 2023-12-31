from django.db import models
from django.contrib import admin
from django.utils import timezone
from django.utils.html import format_html
from django.contrib.auth import get_user_model
from django.utils.safestring import mark_safe

User = get_user_model()

class Advertisements(models.Model):
    title = models.CharField("Заголовок", max_length=128)
    description = models.TextField("Описание")
    price = models.DecimalField("Цена", max_digits=10, decimal_places=2)
    auction = models.BooleanField("Торг", help_text="Отметье, если торг уместен")
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, verbose_name='пользователь', on_delete=models.CASCADE)
    image = models.ImageField("Изображение", upload_to="advertisements/", blank=True)

    def __str__(self):
        return f"Advertisement(id={self.id}, title={self.title}, price={self.price})"

    @admin.display(description='Дата создания')
    def created_date(self):
        if self.created_at.date() == timezone.now().date():
            created_time = self.created_at.time().strftime('%H:%M:%S')
            return format_html(
                '<span style="color: green; font-weight: bold">'
                'Сегодня в {}</span>', created_time
            )
        return self.created_at.strftime('%d:%m:%Y в %H:%M:%S')

    @admin.display(description='Дата обновления')
    def update_date(self):
        if self.update_at.date() == timezone.now().date():
            update_time = self.update_at.time().strftime('%H:%M:%S')
            return format_html(
                '<span style="color: blue; font-weight: bold">'
                'Сегодня в {}</span>', update_time
            )
        return self.update_at.strftime('%d:%m:%Y в %H:%M:%S')

    @admin.display(description='Изображение')
    def if_image(self):
        if self.image:
            return mark_safe(u'<a href="{0}" target="_blank"><img src="{0}" width="100"/></a>'.format(self.image.url))
        else:
            return 'Нет изображения'
    if_image.allow_tags = True

    class Meta:
        db_table = "advertisements"