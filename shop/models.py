from django.db import models
from django.urls import reverse
from stdimage.models import StdImageField  #??

class Category(models.Model):
	name = models.CharField(max_length=250, unique=True)
	slug = models.SlugField(max_length=250, unique=True)
	description = models.TextField(blank=True)
	image = models.ImageField(upload_to='category', blank=True)

	class Meta:
		ordering = ('name',)
		verbose_name = 'category'
		verbose_name_plural = 'categories'

	def get_url(self):
		return reverse('shop:products_by_category', args=[self.slug])

	def __str__(self):
		return '{}'.format(self.name)

class Product(models.Model):
	name = models.CharField(max_length=250, unique=True)
	slug = models.SlugField(max_length=250, unique=True)
	description = models.TextField(blank=True)
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	# price = models.DecimalField(max_digits=10, decimal_places=2)
	price = models.DecimalField(max_digits=10, decimal_places=0)



	image = StdImageField(upload_to='product', blank=True, variations={
        'large': (600, 450),
        'thumbnail': (350, 350, True),
        'medium': (450, 450),
    })	
	stock = models.IntegerField()
	available = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ('name',)
		verbose_name = 'product'
		verbose_name_plural = 'products'

	def get_url(self):
		return reverse('shop:ProdCatDetail', args=[self.category.slug, self.slug])

	def __str__(self):
		return '{}'.format(self.name)



class ProductImage(models.Model):

	name = models.CharField(max_length=250, unique=True)
	image = StdImageField(upload_to='product', blank=True, variations={
        'large': (600, 450),
        'thumbnail': (100, 100, True),
        'medium': (450, 450),
    })	
	product = models.ForeignKey(Product, on_delete=models.CASCADE)	
	created = models.DateTimeField(auto_now_add=True)	
	updated = models.DateTimeField(auto_now=True) 	
   
	class Meta:		
		ordering = ('updated',)		
		verbose_name = 'image'		
		verbose_name_plural = 'images' 

	def __str__(self):		
		return '{}'.format(self.name)


