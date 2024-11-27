from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    Address = models.CharField(max_length=100)

    def __str__(self):
        return self.name
class StuBook(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Student,on_delete=models.CASCADE,related_name='book')

    def __str__(self):
        return self.title

class StuReview(models.Model):
    book = models.ForeignKey(StuBook,on_delete=models.CASCADE,related_name='review')    
    r_text = models.TextField()

    def __str__(self):
        return self.book.title