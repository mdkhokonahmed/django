from django.db import models
# Create your models here.
class Category(models.Model):
	categoryName = models.CharField(max_length=30)
	status = models.IntegerField(default=0)
	def __str__(self):
		return self.categoryName

class Post(models.Model):
	title = models.CharField(max_length=250)
	description = models.TextField()
	cur_date = models.DateTimeField(auto_now_add=True)
	image = models.ImageField()
	category = models.ForeignKey(
		Category,
		models.SET_NULL,
		blank=True,
		null=True,
		)
	def __str__(self):
		return self.title

class Slider(models.Model):
	title = models.CharField(max_length=250)
	image = models.ImageField()

	def __str__(self):
		return self.title

class Logo(models.Model):
	title = models.CharField(max_length=250)
	description = models.CharField(max_length=250)
	image = models.ImageField()

	def __str__(self):
		return self.title
	

		

		
		