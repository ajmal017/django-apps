#*========================== #
#*  Author:		 Dave Luke Jr
#*  Company:	 CenterStack.io
#*  Description:	 animations/views.py
#*========================== #

from django.shortcuts import render


def navigation(request, url):
	url = "animations/%s" % url 
	return render(request, url)