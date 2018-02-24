from django.db import models

# Create your models here.
class Location(models.Model):
  place = models.CharField(max_length=30)

  def __str__(self):
      return self.place

  class Meta:
      ordering = ['place']

  def save_location(self):
      self.save()


class Category(models.Model):
  category = models.CharField(max_length=30)

  def __str__(self):
      return self.category

  def save_category(self):
      self.save()

  @classmethod
  def search_by_category(cls, search_category):
      category = cls.objects.filter(category__icontains=search_category)
      return category


class Gallery(models.Model):
  image = models.ImageField(upload_to='gallery/', null=True, blank=True)
  image_name = models.CharField(max_length=25)
  description = models.TextField(max_length=100)
  location = models.ForeignKey(Location,null=True)
  category = models.ForeignKey(Category, null=True)

  def __str__(self):
      return self.image_name

  @classmethod
  def my_images(cls):
      images = cls.objects.all()
      return images

  def save_images(self):
      self.save()

  def delete_images(self):
      self.remove()

  def update_image(self, id):
      pass

  def get_image_by_id(id):
      pass

  def filter_by_location(location):
      pass

  def search_image(category):
      pass
