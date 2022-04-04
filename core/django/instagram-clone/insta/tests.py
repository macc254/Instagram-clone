from django.test import TestCase
from .models import Image, Profile

# Create your tests here.
class ImageTestClass(TestCase):

    # Set up method
    def setUp(self):
        Image.objects.create(name = 'rara', caption ='air-Lord',image ='juice.jpeg',likes='5',comments='hei')

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.rara,Image))
     # Testing Save Method
    def test_save_image(self):
        self.image.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)
    def tearDown(self):
        Profile.objects.all().delete()
        Image.objects.all().delete()
    def test_instance(self):
        self.assertTrue(isinstance(self.image,Image))
        self.assertTrue(isinstance(self.profile, Profile))