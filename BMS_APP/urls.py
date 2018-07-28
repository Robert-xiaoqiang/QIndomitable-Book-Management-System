from django.conf.urls import url
from . import views
urlpatterns = [
	url(r'^$', views.index, name = 'index'),
	url(r'^user/(?P<user_id>\d+)/$', views.user, name = 'user'),
	#url(r'^new_user/$', views.new_user, name = 'new_user'),
	#url(r'^old_user/$', views.old_user, name = 'old_user'),
	url(r'^user/(?P<user_id>\d+)/reader/$', views.reader, name = 'reader'),
	url(r'^user/(?P<user_id>\d+)/search/$', views.search, name = 'search'),
	url(r'^user/(?P<user_id>\d+)/borrow_history/$', views.borrow_history, name = 'borrow_history'),
	url(r'^user/(?P<user_id>\d+)/registering/(?P<reader_id>\d+)/$', views.registering, name = 'registering'),
	url(r'^user/(?P<user_id>\d+)/card_register/$', views.card_register, name = 'card_register'),
	url(r'^user/(?P<user_id>\d+)/(?P<book_id>\d+)/choose/$', views.choose, name = 'choose'),
	url(r'^user/(?P<user_id>\d+)/(?P<book_id>\d+)/borrow/(?P<card_id>\d+)/$', views.borrow, name = 'borrow'),
]