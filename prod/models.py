from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from PIL import Image


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='products')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    cost_price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='product_images/', null=True, blank=True)
    video = models.FileField(upload_to='product_videos/', null=True, blank=True,)
    date_post = models.DateField(default=timezone.now)

    def __str__(self):
        return self.name
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.image:
            img = Image.open(self.image.path)

            # Set maximum size for the image
            max_size = (500, 500)
            img.thumbnail(max_size)

            # Save the resized image
            img.save(self.image.path)

