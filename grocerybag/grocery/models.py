from django.db import models
from django.conf import settings


# Create your models here.
class addItem(models.Model):
    STATUS = (
        ('PENDING', 'PENDING'),
        ('BOUGHT', 'BOUGHT'),
        ('NOT AVAILABLE', 'NOT AVAILABLE')
    )
    # author = models.ForeignKey(User, on_delete=models.CASCADE,default="")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default='1',
                             on_delete=models.CASCADE)
    name = models.CharField(max_length=1000)
    quantity = models.CharField(max_length=1000)
    status = models.CharField(max_length=200, default='PENDING', choices=STATUS)
    date = models.DateField(auto_now=True, null=True)

    def __str__(self):
        return self.name
