from django import forms
from posts.models import Post
from groups.models import Group

class GroupForm(forms.ModelForm):

    class Meta:
        model = Group
        fields = ('name','description')
