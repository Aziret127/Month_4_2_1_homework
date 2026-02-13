from django.db import models

# Create your models here.


class Book(models.Model):

    title = models.CharField(max_length=100, verbose_name="название книги")

    description = models.TextField(verbose_name="описание книги")

    image = models.ImageField(upload_to="book/", verbose_name="изображение книги")

    crated_date_lang = models.PositiveIntegerField(verbose_name="год выпуска книги", blank=True)

    created_at = models.DateTimeField(auto_now_add=True,)

    full_name = models.CharField(max_length=150, verbose_name="ФИО Автора", null=True, blank=True)

    boi = models.TextField(verbose_name="биография", blank=True, null=True)

    birth_date = models.DateField(verbose_name="дата рождения", null=True, blank=True)

    name_genre = models.CharField(max_length=100, verbose_name="жанр", null=True, blank=True)

    ratiog = models.PositiveBigIntegerField(verbose_name="оценка 1-10", blank=True, null=True)

    def __str__(self):
         return self.title

    class Meta:
        verbose_name = "книга"
        verbose_name_plural = "книги "

