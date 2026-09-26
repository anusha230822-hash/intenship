from django.db import models

# Create your models here.
class exams(models.Model):
    name = models.CharField(max_length=100)
    score = models.DecimalField(max_digits=10, decimal_places=2)
    date_of_exam = models.DateField()
    time = models.TimeField()
    duration = models.DurationField()


    def __str__(self):
        return self.name