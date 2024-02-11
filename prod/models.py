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
    video = models.FileField(upload_to='product_videos/', null=True, blank=True)
    date_post = models.DateField(default=timezone.now)
    color = models.CharField(max_length=50, null=True, blank=True)
    size = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.name

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


from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Cart for {self.user.username}"
    def total_price(self):
        total = sum(item.product.cost_price * item.quantity for item in self.items.all())
        return total


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)  # Assuming you have a Product model
    quantity = models.PositiveIntegerField(default=1)
    added_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.quantity}x {self.product.name} in cart"
