from django.test import TestCase
from .models import Image, Profile

# Create your tests here.
class ImageTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.rara= Image(name = 'rara', caption ='air-Lord',image ='juice.jpeg',likes='5',comments='hei')
    #Testing  instance
    # def test_instance(self):
    #     self.assertTrue(isinstance(self.rara,Image))
    #  # Testing Save Method
    # def test_save_method(self):
    #     self.rara.save_image()
    #     images = Image.objects.all()
    #     self.assertTrue(len(images) > 0)