from django.db import models
#her bir class db tablosu içindekiler de sütunudur
class Blogs(models.Model):
    Blog_Title = models.CharField(max_length=500)
    Blog_Descripton = models.TextField()
    Blog_Short_Description = models.TextField()
    Blog_Image = models.ImageField(upload_to="blogs/")
    Is_Home = models.BooleanField(default=False)
    Is_Active = models.BooleanField(default=False)

    def __str__(self):
        return self.Blog_Title



