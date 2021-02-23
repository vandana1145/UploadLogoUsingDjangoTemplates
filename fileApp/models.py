from django.db import models

# Create your models class 

class Image(models.Model):
    title = models.CharField(max_length=100, verbose_name="Title")
    logo = models.ImageField(upload_to="images/", verbose_name="Logo")

    def __str__(self):
        return self.title


class Category(models.Model):
    category_name = models.CharField(max_length=100, db_index=True, verbose_name='category_name')

    def __str__(self):
        return str(self.category_name)


class Product(models.Model):
    category_name = models.ForeignKey(Category, related_name='products', verbose_name="category_name", on_delete=models.CASCADE)
    product_name = models.CharField(max_length=100, verbose_name='product_name')
    image = models.ImageField(upload_to='products/', blank=True, verbose_name='image')
    description = models.TextField(blank=True, verbose_name='description')

    def __str__(self):
        return str(self.product_name)
    

class Choice(models.Model):
    product_name = models.ForeignKey(Product, related_name='product', verbose_name='item', on_delete=models.CASCADE)
    size = models.CharField(max_length=4, verbose_name='size')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='price')

    def __str__(self):
        return str(self.product_name),  str(self.size)
    