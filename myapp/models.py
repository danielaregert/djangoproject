from django.db import models
#from django_ckeditor_5.fields import CKEditor5Field

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField() 
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)  # Optional image upload
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
