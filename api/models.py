from django.db import models

class SmartPhone(models.Model):
    price = models.CharField(max_length=30)
    img_url = models.CharField(max_length=255)
    color = models.CharField(max_length=30)
    ram = models.IntegerField()
    memory = models.IntegerField()
    name = models.CharField(max_length=30)
    model = models.CharField(max_length=30)

    def __str__(self):
        return self.name
    
    def to_dict(self):
        returned = {
                'price': self.price,
                'img_url':self.img_url,
                'color':self.color,
                'ram':self.ram,
                'memory':self.memory,
                'name':self.name,
                'model':self.model
            }
        return returned