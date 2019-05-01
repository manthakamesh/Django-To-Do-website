from django.db import models
import django
from django.urls import reverse
# Create your models here.
class todolist(models.Model):
    item=models.CharField(max_length=300)
    created_date=models.DateTimeField(default=django.utils.timezone.now)
    cross=models.BooleanField(default=False)

    def __str__(self):
        return self.item

    def get_absolute_url(self):
        return reverse('all')
