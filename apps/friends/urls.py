from django.conf.urls import url
from views import index,main,show_friends,view_profile,add_friend,remove_friend
from ..login_reg_app.views import login, register, success, logout

urlpatterns = [
    url(r'^$', index),
    url(r'^main$', main),
    url(r'^friends$', show_friends),
    url(r'^user/(?P<id>\d+)$', view_profile),
    url(r'^remove/(?P<id>\d+)$', remove_friend),
    url(r'^add/(?P<id>\d+)$', add_friend),
    url(r'^login$', login),
    url(r'^register$', register),
    url(r'^success$', success),
    url(r'^logout$', logout)
]
