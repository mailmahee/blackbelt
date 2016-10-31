from __future__ import unicode_literals
from django.db import models
from ..login_reg_app.models import User
from django.contrib import messages
from django.db.models import Q


class FriendshipManager(models.Manager):
    def get_complete_context(self,request):

        currentUser = User.objects.get(uemail = request.session['user']['uemail'])

        myFriends = [friendship.to_friend for friendship in currentUser.friend_set.all()]

        excluders = [fships.from_friend.uemail for fships in  currentUser.to_friend_set.all()]
        excluders.append(currentUser.uemail)
        otherUsers = User.objects.exclude(uemail__in = excluders)
        # print otherUsers

        context = {
          "myFriends" : myFriends,
          "otherUsers" : otherUsers
        }
        return context

    def add_friend(self, request,id):
        validation = False

        currentUser = User.objects.get(uemail = request.session['user']['uemail'])
        newFriend = User.objects.get(id = id)

        # //check if the user is already a friends
        validation = Friendship.objects.create(from_friend=currentUser,to_friend=newFriend)
        validation = Friendship.objects.create(from_friend=newFriend,to_friend=currentUser)

        return validation

    def remove_friend(self,request,id):
        validation = False
        currentUser = User.objects.get(uemail = request.session['user']['uemail'])
        remFriend = User.objects.get(id = id)

        # check if the relationship exists before removing the friendship
        validation = Friendship.objects.filter(from_friend=currentUser,to_friend=remFriend).delete()
        validation = Friendship.objects.filter(from_friend=remFriend,to_friend=currentUser).delete()

        return validation

    def view_profile(self,request,id):
        currentUser = User.objects.get(id = id)

        context = {
        "uname" : currentUser.uname,
        "name" : currentUser.name,
        "uemail" : currentUser.uemail
        }

        return context

# Create your models here.
class Friendship(models.Model):
    from_friend = models.ForeignKey(User, related_name='friend_set')
    to_friend = models.ForeignKey(User, related_name='to_friend_set')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = FriendshipManager()
    class Meta:
        unique_together = (('to_friend', 'from_friend'),)
    # def __unicode__(self):
    #     return u'%s, %s' % (self.from_friend.uemail,self.to_friend.uemail)
