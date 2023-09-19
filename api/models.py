from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=200)
    age = models.PositiveIntegerField()
    description = models.TextField()
    date_enrolles = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return super().__str__()
