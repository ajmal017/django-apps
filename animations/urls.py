#*====================== #
#*  Author:	Dave Luke Jr
#*  Company:	CenterStack.io
#*  Description:	app/urls.py
#*====================== #

from django.conf.urls import patterns, url, include

# ==================================================#
#	Pages URL Conf
# ==================================================#
urlpatterns = patterns('',
	url(r'^$', 'animations.views.navigation', {"url":"index.html"}, name="animations_index"),
	url(r'^hover/$', 'animations.views.navigation', {"url":"hover.html"}, name="animations_hover"),
	url(r'^animate/$', 'animations.views.navigation', {"url":"animate.html"}, name="animations_animate"),
	url(r'^animations/$', 'animations.views.navigation', {"url":"animations.html"}, name="animations_animations"),
)



	

