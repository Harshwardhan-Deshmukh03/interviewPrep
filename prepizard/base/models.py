from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager
from django.contrib.auth.models import User 



class Student(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    college = models.CharField(max_length=200, null=True)
    score = models.IntegerField(default=0)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self) -> str:
        return self.name




class Course(models.Model):
    course_name = models.CharField(max_length=100)
    course_description = models.TextField()

    def __str__(self):
        return self.course_name

class Question(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    question_text = models.TextField()
    option1 = models.CharField(max_length=200)
    option2 = models.CharField(max_length=200)
    option3 = models.CharField(max_length=200)
    option4 = models.CharField(max_length=200)
    correct_option = models.IntegerField()

    def __str__(self):
        return self.question_text



class Resource(models.Model):
    resource_name = models.CharField(max_length=100)
    resource_description = models.TextField()
    resource_material=models.CharField(max_length=15000)

    def __str__(self):
        return self.resource_name


class Attempt(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    attempted = models.BooleanField(default=False)
    correct_attempt = models.BooleanField()
    def __str__(self):
        return f"{self.student.first_name}'s attempt on {self.question}"
    

class Room(models.Model):
    name=models.CharField(max_length=255)
    slug=models.SlugField(unique=True)

    def __str__(self):
        return self.name
    

class Message(models.Model):
    room=models.ForeignKey(Room,related_name='messages',on_delete=models.CASCADE)
    user=models.ForeignKey(User,related_name='messages',on_delete=models.CASCADE)
    content=models.TextField()
    date_added=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user
    class Meta:
        ordering=('date_added',)



class CheatSheet(models.Model):
    topic_name = models.CharField(max_length=200)
    description = models.TextField()
    pdf_file = models.FileField(upload_to='cheat_sheets/')

    def __str__(self):
        return self.topic_name
