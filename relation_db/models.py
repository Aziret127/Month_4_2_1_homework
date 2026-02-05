from django.db import models

# Create your models here.

class category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Person(models.Model):
    userr = models.CharField(max_length=100, default=" ")
    category = models.ManyToManyField(category, null=True)
    def  __str__(self):
        return f'{self.userr} --- {','.join(i.name for i in self.category.all())}'

class tourk(models.Model):
    choice_tour = models.OneToOneField(Person, on_delete=models.CASCADE, related_name="tour" )
    TYPEOFTOURS = (
        ('Круизный тур', "Круизный тур"),
        ("этнический тур","этнический тур"),
        ("религиозный тур","религиозный тур"),
        ("образавательный тур","образавательный тур"),
    )
    typeoftours = models.CharField(max_length=100, choices=TYPEOFTOURS,)

    def __str__(self):
        return self.typeoftours
    
class Review(models.Model):
    TOURS = (
        ("Отличный", "Отличный"),
        ("Лучший","Лучший"),
        ("Одекватный","Одекватный"),
        ("НЕ НОРМАЛЬНЫЙ","НЕ НОРМАЛЬНЫЙ"),
    )
    tours = models.CharField(max_length=100, choices=TOURS, )
    choice_tour = models.OneToOneField(Person, on_delete=models.CASCADE, related_name="review" )
    
    
    def __str__(self):
        return f'выбор турав:{self.choice_tour}-оценка клиента:{self.tours}'