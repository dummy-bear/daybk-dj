from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
from taggit.managers import TaggableManager
from django.contrib.auth.models import User

class Task(models.Model):
	userID = models.ForeignKey(User, on_delete=models.CASCADE)
	name = models.CharField(max_length=2000)
	url = models.SlugField()
	tcreate = models.DateTimeField(auto_now_add=True)
	tstart = models.DateTimeField(null=True)
	tfinish = models.DateTimeField(null=True)
	deadline = models.DateTimeField(null=True)
	approxtime = models.IntegerField()
	condit = models.CharField(max_length=2)
	priority = models.IntegerField()
	description = RichTextUploadingField()
	uptasks = models.TextField()
	subtasks = models.TextField()
	collapse = models.CharField(max_length=2,default='y')
	
	
	def __str__(self):
		return self.name

class Plan(models.Model):
	userID = models.ForeignKey(User, on_delete=models.CASCADE)
	taskID = models.ForeignKey(Task, on_delete=models.CASCADE)
	tstart = models.DateTimeField(null=True)
	tfinish = models.DateTimeField(null=True)
	public = models.CharField(max_length=2,default='u')
	typ = models.CharField(max_length=2,default='u')
	
	def __str__(self):
		return str(self.taskID)

class Post(models.Model):
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	task = models.ForeignKey(Task, on_delete=models.SET_NULL,blank=True,null=True)
	url = models.SlugField()
	title = models.CharField(max_length=2000)
	description = RichTextUploadingField()
	content = RichTextUploadingField()
	image = models.ImageField()
	created_at = models.DateTimeField(auto_now_add=True)
	tag = models.CharField(max_length=2000)
	tstart = models.DateTimeField(null=True)
	tstop = models.DateTimeField(null=True)
	waistedtime = models.IntegerField(default=0)
	public = models.CharField(max_length=2,default='u')
	typ = models.CharField(max_length=2,default='u')
	
	def __str__(self):
		return self.title
		
# Create your models here.
