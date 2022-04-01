from django.test import TestCase
from .models import Image, Profile

# Create your tests here.
class ImageTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.roku= Image(name = 'roku', caption ='Fire-Lord')
    #Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.roku,Image))
     # Testing Save Method
    def test_save_method(self):
        self.roku.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)