from django.db import models

class Organization(models.Model):
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    organic_name = models.CharField(max_length=100, blank=True, default="")
    image = models.CharField(max_length=300, blank=True, default="")
    free_course_open = models.CharField(max_length=3, default="0", blank=True)
