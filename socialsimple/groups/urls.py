
from django.urls import include,path
from . import views


app_name = 'groups'

urlpatterns = [
    path('grouplist', views.GroupListView.as_view(), name='group-list'),
    path('groupcreate', views.GroupCreate.as_view(), name='groupcreate'),
    path('groupdetail/<slug>', views.GroupViewDetails.as_view(), name='groupdetail'),
    path('joingroup', views.JoinGroup.as_view(), name='join'),
    path('leavegroup', views.LeaveGroup.as_view(), name='leave'),

    ]
