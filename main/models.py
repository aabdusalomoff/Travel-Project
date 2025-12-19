from django.db import models
from django.utils.text import slugify


class Country(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True) 
    desc = models.TextField()
    population = models.DecimalField(max_digits=5, decimal_places=2)
    territory = models.DecimalField(max_digits=10, decimal_places=3)
    price = models.DecimalField(max_digits=10, decimal_places=3)
    image = models.FileField(upload_to="images")
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title