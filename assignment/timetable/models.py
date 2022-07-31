from django.db import models

# Create your models here.
class TimeTable(models.Model):
    course_title = models.CharField(max_length=2000)
    course_code = models.CharField(max_length=6)
    hall = models.CharField(max_length=200)
    time = models.CharField(max_length=20)
    invigilators = models.CharField(max_length=2000)
    department = models.CharField(max_length=200)

    def __str__(self):
        return self.course_title