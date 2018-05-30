from django.db import models
from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Category(models.Model):
	title = models.CharField(max_length=100, unique=True)

	def __str__(self):
		return self.title

class blog(models.Model):
	title = models.CharField(max_length=100, unique=True)
	# slug = models.slugField(max_length=100, unique=True)
	body = models.TextField()
	posted = models.DateField(db_index=True, auto_now_add=True)
	category = models.ManyToManyField(Category, help_text='Select a category for this post')
	author = models.ForeignKey('Author', on_delete=models.CASCADE)

	class Meta:
		ordering = ["-posted"]


	def get_link(self):
		return self.pk

	def __str__(self):
		return self.title




class Author(models.Model):
	user = models.OneToOneField(
		User,
		on_delete=models.CASCADE,
		primary_key=True,
		)
	first_name = models.CharField(max_length=100, null=True)
	last_name = models.CharField(max_length=100, null=True)
	date_of_birth = models.DateField(null=True, blank=True)
	date_of_death = models.DateField('Died', null=True, blank=True)

	# class Meta:
	# 	ordering = ["last_name","first_name"]

	def get_absolute_url(self):

		return reverse('author-detail', args=[str(self.id)])

	def __str__(self):
		return '{0}, {1}'.format(self.last_name,self.first_name)