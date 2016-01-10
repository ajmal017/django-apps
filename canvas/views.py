#*====================== #
#*  Author:		 Dave Luke Jr
#*  Company:	 CenterStack.io
#*  Description:	 canvas/views.py
#*====================== #

from django.shortcuts import render


def navigation(request, url):
	url = "canvas/%s" % url
	return render(request, url)