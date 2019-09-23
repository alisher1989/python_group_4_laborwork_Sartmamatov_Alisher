from django.db import models

PRODUCT_OTHER_CHOICE = 'other'
PRODUCT_CATEGORY_CHOICES = (
    (PRODUCT_OTHER_CHOICE, 'other'),
    ('food', 'food'),
    ('drink', 'drink'),
    ('cloth', 'cloth'),
    ('sport', 'sport'),
    ('shoes', 'shoes')
)


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='name')
    description = models.TextField(max_length=2000, verbose_name='description', null=True, blank=True)
    category = models.CharField(max_length=20, verbose_name='category', choices=PRODUCT_CATEGORY_CHOICES, default=PRODUCT_OTHER_CHOICE)
    amount = models.PositiveIntegerField(verbose_name='amount')
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='price')


    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Items'
