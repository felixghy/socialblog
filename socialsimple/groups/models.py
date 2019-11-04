from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
import misaka as m
from django.utils.text import slugify
from django.urls import reverse
from django import  template

#register = template.Library()

# Create your models here.

class Group(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.CharField(max_length=255,unique=True)
    description = models.TextField(blank=True,default='')
    description_html = models.TextField(editable=False,default='',blank=True)

    members = models.ManyToManyField(User,through='GroupMember')

    def __str__ (self):
        return self.name

    def save (self, *args, **kwargs):
        self.slug = slugify(self.name)
        self.description = m.html(self.description)
        print(f'----------group description_html is {self.description}-------')
        super().save(args,kwargs)

    def get_absolute_url(self):
        # F: question
        return reverse('groups:groupdetail',kwargs={'slug':self.slug})
        # return reverse('groups:groupdetail', kwargs={'pk': self.pk})


    class Meta:
        ordering =['-name']

class GroupMember(models.Model):
    group = models.ForeignKey(Group,related_name='memberships', on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User,related_name='user_groups',on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.user.username

    class Meta:
        unique_together=['group','user']
