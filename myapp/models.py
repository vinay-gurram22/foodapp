from django.db import models

# Create your models here.
class Item(models.Model):

    def __str__(self):
        return self.item_name

    item_name = models.CharField(max_length=200)
    item_desc = models.CharField(max_length=500)
    item_price = models.IntegerField()
    item_image = models.CharField(max_length=500,default="https://dynamic-media-cdn.tripadvisor.com/media/photo-o/2b/5e/1b/ba/join-us-for-a-delightful.jpg?w=900&h=500&s=1")


