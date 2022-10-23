from django.urls import reverse
from django.db import models

# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(max_length = 250, blank=True)
    cat_image = models.ImageField(upload_to="uploads/categories", blank=True)

    def __str__(self) -> str:
        return self.category_name

    # def get_url(self):
    #     return reverse("products-by-category", args=[self.slug])
    

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

