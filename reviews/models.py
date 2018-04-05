from django.db import models
from django.contrib.auth.models import User

# class review(models.Model):
#     author = models.ForeignKey(User, on_delete=models.CASCADE)
#     pub_date = models.DateTimeField('date published', auto_now=True)
#     text_before = models.CharField(max_length=200, verbose_name='Текст до', help_text='полезная инфа', blank=True, null=True)
#     text_after = models.CharField(max_length=200)
#
#     class Meta:
#         verbose_name = "Ревью"
#         verbose_name_plural = "Ревью"
#
#     def __str__(self):
#         return self.text_after

class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    class Meta:
        verbose_name = "Комментатор"
        verbose_name_plural = "Комментаторы"

class Review(models.Model):
    author = models.ForeignKey(Person, on_delete=models.CASCADE, related_name="Комментаторы" )
    pub_date = models.DateTimeField('date published', auto_now=True)
    text_before = models.CharField(max_length=200, verbose_name='Текст до', help_text='Текст до редактирования', blank=True, null=True)
    text_after = models.CharField(max_length=200, verbose_name='Текст после', help_text='Текст после авторедактирования', blank=True, null=True)

    class Meta:
        verbose_name = "Ревью"
        verbose_name_plural = "Ревью"

    def __str__(self):
        return self.text_before

class DictCurse(models.Model):
    text = models.CharField(max_length=15)

    class Meta:
        verbose_name = "Матерное слово"
        verbose_name_plural = "Матерные слова"

    def __str__(self):
        return self.text

class DictExceptions(models.Model):
    text = models.CharField(max_length=15)

    class Meta:
        verbose_name = "Не матерное слово"
        verbose_name_plural = "Не матерные слова"

    def __str__(self):
        return self.text
