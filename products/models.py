from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.
class Product(models.Model):
    '''
    Holds details of a product
    '''
    hunter = models.ForeignKey(
        User,
        null=True,
        on_delete=models.CASCADE)
    title = models.CharField(
        max_length=100,
        blank=False)
    url = models.TextField(
        max_length=2000,
        blank=False)
    pub_date = models.DateTimeField(
        blank=False,
        null=False,
        auto_now_add=True)
    votes_total = models.IntegerField(
        default=1)
    image = models.ImageField(default='product_pics/default.jpg',
                              upload_to='product_pics',
                              blank=True,
                              null=True)
    icon = models.ImageField(default='product_pics/default.jpg',
                              upload_to='product_pics',
                              blank=True,
                              null=True)
    body = models.TextField(
        max_length=2000,
        blank=False)

    def pub_date_beautify(self):
        '''
        Beautifies the pub_date and makes it a more
        presentable format using strftime
        '''
        return self.pub_date.strftime('%e %b %Y')

    def __str__(self):
        return "#{0} [{1} - {2}] - {3}".format(
            self.id, self.title)
