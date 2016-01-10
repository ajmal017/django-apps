#*========================= #
#*  Author:	Dave Luke Jr
#*  Company:	CenterStack.io
#*  Description:	metronic/views.py
#*========================= #
import os
from django.shortcuts import render


APP_DIR = os.path.dirname(os.path.abspath(__file__))
APP_NAME = os.path.basename(APP_DIR)


def navigation(request, template):
	url = os.path.join(APP_NAME, template)
	return render(request, url)

# def admin(request, template, N=1):
# 	directory = "admin_%s" % N
# 	url = os.path.join(APP_NAME, directory, template)
# 	return render(request, url)








