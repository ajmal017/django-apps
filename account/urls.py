#*====================== #
#*  Author:		 Dave Luke Jr
#*  Company:	 CenterStack.io
#*  Description:	 account/urls.py
#*====================== #

from django.conf.urls import patterns, url, include

# ==================================================#
#	Login & Register
# ==================================================#
urlpatterns = patterns('',
	url(r'^login/$', 'django.contrib.auth.views.login', {"template_name":"login.html"}, name="account-login"),
	url(r'^logout/$', 'django.contrib.auth.views.logout', name="account-logout"),
	url(r'^profile/$', 'account.views.profile', {"url":"profile.html"}, name="account-profile"),
)








	

