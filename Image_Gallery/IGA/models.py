from django.db import models


Category = (
    ('nature','Nature'),
    ('animals', 'Animals'),
    ('fruits','Fruits'),
)

class Image(models.Model):
    category = models.CharField(max_length=50, choices=Category, default='nature')
    image = models.ImageField(upload_to='images/')
    created = models.DateTimeField(auto_now_add=True)

