from django.db import models

# Create your models here.
'''class sample(models.Model):
    
    category_id=models.IntegerField()
    category_name=models.CharField(max_length=50,null=True)
    @property
    def category_id(self):
       return self.id+100
    
    def __str__(self):
        return self.category_name'''