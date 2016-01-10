#*====================== #
#*  Author:		 Dave Luke Jr
#*  Company:	 CenterStack.io
#*  Description:	 pages/urls.py
#*====================== #
from django.conf.urls import patterns, url, include

# ==================================================#
#	Pages URL Conf
# ==================================================#
urlpatterns = patterns('',
	url(r'^404/$', 'pages.views.navigation', {"template":"404.html"}, name="pages-404"),
	url(r'^404/$', 'pages.views.navigation', {"template":"404.html"}, name="pages-404"),
	url(r'^500/$', 'pages.views.navigation', {"template":"500.html"}, name="pages-500"),
	url(r'^blank_template/$', 'pages.views.navigation', {"template":"blank-template.html"}, name="pages-blank-template"),
	url(r'^boxed_layout/$', 'pages.views.navigation', {"template":"boxed-layout.html"}, name="pages-boxed-layout"),
	url(r'^builder/$', 'pages.views.navigation', {"template":"builder.html"}, name="pages-builder"),
	url(r'^buttons/$', 'pages.views.navigation', {"template":"buttons.html"}, name="pages-buttons"),
	url(r'^calendar/$', 'pages.views.navigation', {"template":"calendar.html"}, name="pages-calendar"),
	url(r'^charts/$', 'pages.views.navigation', {"template":"charts.html"}, name="pages-charts"),
	url(r'^color/$', 'pages.views.navigation', {"template":"color.html"}, name="pages-color"),
	url(r'^datatables/$', 'pages.views.navigation', {"template":"datatables.html"}, name="pages-datatables"),
	url(r'^email/$', 'pages.views.navigation', {"template":"email.html"}, name="pages-email"),
	url(r'^email_compose/$', 'pages.views.navigation', {"template":"email-compose.html"}, name="pages-email-compose"),
	url(r'^form_elements/$', 'pages.views.navigation', {"template":"form-elements.html"}, name="pages-form-elements"),
	url(r'^form_layouts/$', 'pages.views.navigation', {"template":"form-layouts.html"}, name="pages-form-layouts"),
	url(r'^form_wizard/$', 'pages.views.navigation', {"template":"form-wizard.html"}, name="pages-form-wizard"),
	url(r'^gallery/$', 'pages.views.navigation', {"template":"gallery.html"}, name="pages-gallery"),
	url(r'^google_map/$', 'pages.views.navigation', {"template":"google-map.html"}, name="pages-google-map"),
	url(r'^icons/$', 'pages.views.navigation', {"template":"icons.html"}, name="pages-icons"),
	url(r'^index/$', 'pages.views.navigation', {"template":"index.html"}, name="pages-index"),
	url(r'^invoice/$', 'pages.views.navigation', {"template":"invoice.html"}, name="pages-invoice"),
	url(r'^lock_screen/$', 'pages.views.navigation', {"template":"lock-screen.html"}, name="pages-lock-screen"),
	url(r'^login/$', 'pages.views.navigation', {"template":"login.html"}, name="pages-login"),
	url(r'^modals/$', 'pages.views.navigation', {"template":"modals.html"}, name="pages-modals"),
	url(r'^nestables/$', 'pages.views.navigation', {"template":"nestables.html"}, name="pages-nestables"),
	url(r'^notifications/$', 'pages.views.navigation', {"template":"notifications.html"}, name="pages-notifications"),
	url(r'^portlets/$', 'pages.views.navigation', {"template":"portlets.html"}, name="pages-portlets"),
	url(r'^progress/$', 'pages.views.navigation', {"template":"progress.html"}, name="pages-progress"),
	url(r'^register/$', 'pages.views.navigation', {"template":"register.html"}, name="pages-register"),
	url(r'^sliders/$', 'pages.views.navigation', {"template":"sliders.html"}, name="pages-sliders"),
	url(r'^social/$', 'pages.views.navigation', {"template":"social.html"}, name="pages-social"),
	url(r'^tables/$', 'pages.views.navigation', {"template":"tables.html"}, name="pages-tables"),
	url(r'^tabs_accordian/$', 'pages.views.navigation', {"template":"tabs-accordian.html"}, name="pages-tabs-accordian"),
	url(r'^timeline/$', 'pages.views.navigation', {"template":"timeline.html"}, name="pages-timeline"),
	url(r'^tree_view/$', 'pages.views.navigation', {"template":"tree-view.html"}, name="pages-tree-view"),
	url(r'^typography/$', 'pages.views.navigation', {"template":"typography.html"}, name="pages-typography"),
	url(r'^vector_map/$', 'pages.views.navigation', {"template":"vector-map.html"}, name="pages-vector-map"),
)