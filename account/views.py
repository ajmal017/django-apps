#*====================== #
#*  Author:		 Dave Luke Jr
#*  Company:	 CenterStack.io
#*  Description:	 account/views.py
#*====================== #

from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def navigation(request, url):
	url = "account/%s" % url
	return render(request, url)

@login_required
def profile(request):
	url = "account/profile.html"
	return render(request, url)










