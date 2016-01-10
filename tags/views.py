from django.shortcuts import render

def navigation(request, url):
	url = "templates/%s" % url 
	return render(request, url)