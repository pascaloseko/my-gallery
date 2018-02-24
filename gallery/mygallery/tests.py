from django.test import TestCase
from .models import Gallery,Location,Category
# Create your tests here.
class GalleryTestClass(TestCase):

      # Set up method
      def setUp(self):
            self.mygallery=Gallery(image_name='my awesome wb Gallery',description='brilliant and top of the pops')

      # Testing  instance
      def test_instance(self):
            self.assertTrue(isinstance(self.mygallery,Gallery))

      # Testing Save Method
      def test_save_method(self):
            self.mygallery.save_images()
            gallery = Gallery.objects.all()
            self.assertTrue(len(gallery) > 0)
