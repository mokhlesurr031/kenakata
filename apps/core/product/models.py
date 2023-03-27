from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name


OFFER_CHOICES = (
    ('flat', 'Flat'),
    ('percentage', 'Percentage'),
)


class Product(models.Model):
    name = models.CharField(max_length=300)
    price = models.FloatField(default=0.0)
    image = models.ImageField(upload_to='upload/images/')
    description = models.TextField()
    is_offer_running = models.BooleanField(default=False)
    offer_type = models.CharField(max_length=15, choices=OFFER_CHOICES, default='flat')
    offer_rate = models.FloatField(default=0.0)
    price_including_offer = models.FloatField(default=0.0)
    category = models.ForeignKey(Category,related_name='category',on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name
