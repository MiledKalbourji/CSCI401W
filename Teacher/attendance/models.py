from django.db import models

# Create your models here.
# models.py

class Attendance(models.Model):
    student_name = models.CharField(max_length=100)
    student_id = models.CharField(max_length=100)
    date = models.DateField()
    present = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.student_name} - {self.date}"

