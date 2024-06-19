from django.db import models
from django.urls import reverse

class Posts(models.Model):
    title=models.CharField(max_length=255)
    content=models.CharField(max_length=500)
    price=models.CharField(max_length=500,null=True)
    is_publicated=models.BooleanField(blank=True, default=True)
    photo=models.ImageField(upload_to='photos/%Y/%m/%d')
    time_update = models.DateTimeField(auto_now=True)
    time_create = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey('category',on_delete=models.PROTECT, null=True)
  

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id': self.pk})
    
class category(models.Model):
    name=models.CharField(max_length=255,db_index=True, verbose_name='Имя')
    slug=models.SlugField(max_length=255,db_index=True,unique=True,verbose_name="Ссылка")
     
    def __str__(self):
        return self.name

    def get_absolute_url(self):
            return reverse('category', kwargs={'category_id': self.pk})