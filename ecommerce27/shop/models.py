from django.db import models

# Create Category models here
class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=100, null=True, blank=True)
    desc = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    image = models.ImageField(upload_to='Category/images/')

# To display saved Category name in DB instead of Object1, Object 2 ect
    def __str__(self):
        return self.name

# Create Product models here
class Product(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, null=True, blank=True)
    desc = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    categ_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    image = models.ImageField(upload_to='Product/images/')
    availability = models.BooleanField(default=True)
    stock_qty = models.IntegerField()

# To display saved Product name in DB instead of Object1, Object 2 ect
    def __str__(self):
        return self.name

