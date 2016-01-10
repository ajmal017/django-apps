#*========================== #
#*  Author:		Dave Luke Jr
#*  Company:	CenterStack.io
#*  Description:	Convert to Static
#*========================== #
import os, sys, codecs, re, shutil, zipfile, urllib2, urllib
from pprint import pprint as pp
import bs4, pyautogui
from django.conf import settings
sys.stdout = codecs.getwriter('utf8')(sys.stdout)



# ==================================================#
#	Variables Class
# ==================================================#
class InitVariables():
	def __init__(self):
		self.PARSER				= "lxml"											# Parser Options: html.parser, lxml, html5lib
		self.AUTHOR				= "CenterStack"										# What you want the meta.author.content tag to equal
		self.TITLE					= "default"											# What you want the meta.title.string to equal
		self.STATIC					= "{% load staticfiles %}"								# Django load statement for static files
		self.TEMPLATE_FOLDER		= "/sys/centerstack/projects/bond6/site/apps/canvas/templates"	# Folder that contains all your template HTML files
		self.TEMPLATE_FILES 			= self.get_files(self.TEMPLATE_FOLDER)						# List of template HTML files in the TEMPLATES_FOLDER
		self.TEMPLATE_BACKUP_ZIP	= "/sys/centerstack/materials/templates/canvas/templates.zip"		# Backup .zip file of all original template HTML files

	def get_files(self, dir):
		files = []
		filesbase = []
		for file in os.listdir(dir):
			filename = os.path.join(dir,file)
			filenamebase = os.path.basename(os.path.join(dir,file))
			if os.path.isfile(filename):
				if filenamebase[0] != ".":
					files.append(filename)
					filesbase.append(filenamebase)
		return files


	def src_type(self, src):
		



		# if nav_a_href[0:4] != "http":
		# 	if nav_a_href[0] == "#":
		# 		nav_a['href'] = "#"
		# 	elif nav_a_href[0:2] == "tel":
		# 		pass
		# 	else:


# ==================================================#
#	Compile Source to Django Static Tags
# ==================================================#
class CompileStatic():
	def __init__(self):
		self.var = InitVariables()

	def create_soup(self, template):
		self.f = open(template,'r+')
		self.soup = bs4.BeautifulSoup(self.f, self.var.PARSER,from_encoding="utf-8")
			
	def load_static(self):
		try:
			html_tag = self.soup.find("html")
			html_tag.insert_before(self.var.STATIC)
		except:
			pass

	def compile_meta(self):
		try:
			self.soup.find("meta",{"name":"author"})['content'] = self.var.AUTHOR
			if self.var.TITLE == "default":
				pass
			else:
				self.soup.find("title").string = self.var.TITLE
		except:
			pass

	def compile_css(self):
		try:
			links = self.soup.find_all("link")
			for link in links:
				href = link['href']
				if href[0:7] != "http://":
					django_static_link = "{%% static '%s' %%}" % href
					link['href'] = django_static_link
		except:
			pass

	def compile_js(self):
		try:
			scripts = self.soup.find_all("script")
			for script in scripts:
				try:
					src = script['src']
					if src[0:7] != "http://":
						django_static_src = "{%% static '%s' %%}" % src
						script['src'] = django_static_src
				except:
					pass
		except:
			pass

	def compile_img(self):
		try:
			imgs = self.soup.find_all("img")
			for img in imgs:
				img_src = img['src']
				if img_src[0:7] != "http://":
					django_static_img = "{%% static '%s' %%}" % img_src
					img['src'] = django_static_img
		except:
			pass

	def compile_logo(self):
		try:
			ddls = self.soup.find_all(attrs={'data-dark-logo' : True})
			for ddl in ddls:
				logo = ddl['data-dark-logo']
				if logo[0:7] != "http://":
					logo_new = "images/logo-transparent.png"
					ddl['data-dark-logo'] = "{%% static '%s' %%}" % logo_new
		except:
			pass

	def compile_nav(self):
		try:
			nav_tags = self.soup.find("nav").find_all("a")
			for nav_a in nav_as:
				try:
					nav_a_href = nav_a['href']
					if nav_a_href[0:4] != "http":
						if nav_a_href[0] == "#":
							nav_a['href'] = "#"
						elif nav_a_href[0:2] == "tel":
							pass
						else:
							url = nav_a_href[0:nav_a_href.find(".html")]
							nav_a['href'] = "{%% url '%s' %%}" % url.replace("-", "_")
				except:
					pass
		except:
			pass

	def compile_a(self):
		try:
			a_tags = self.soup.find_all("a")
			for a_tag in a_tags:
				ahref = a_tag['href']
				if ahref[0:7] != "http://" and ahref[0] != "#" and ahref[0:3] != "tel" and ahref[0:2] != "{%":
					url = ahref[0:ahref.find(".html")]
					if url[-5:] == ".html":
						a_tag['href'] = "{%% url '%s' %%}" % url.replace("-", "_")
					else:
						a_tag['href'] = "{%% static '%s' %%}" % ahref
		except:
			pass


	#	Save
	# ========================================= #
	def save(self, template):
		try:
			self.f.close()
			html = self.soup.prettify("utf-8")
			with open(template, "wb") as file:
				 file.write(html)
		except:
			pass


	#	Main Loop through all templates
	# ========================================= #
	def loop(self):
		try:
			for template_file in self.var.TEMPLATE_FILES:
				self.create_soup(template_file)
				if re.search(self.var.STATIC, self.soup.prettify()):
					print "%s --- Already Processed! Skipping..." % os.path.basename(template_file)
					continue
				else:
					self.load_static()
					self.compile_meta()
					self.compile_css()
					self.compile_js()
					self.compile_img()
					self.compile_logo()
					self.compile_nav()
					self.compile_a()
					self.save(template_file)
					print os.path.basename(template_file)
			print "Process Complete!"
		except Exception, e:
			print e

# ==================================================#
#	URL Conf
# ==================================================#
class urlconf():
	def __init__(self):
		self.var = InitVariables()

	def generate_urlconf(self):
		nav_as = self.soup.find("nav").find_all("a")
		for nav_a in nav_as:
			try:
				nav_a_href = nav_a['href']
				if nav_a_href[0:7] != "http://":
					if nav_a_href[0] != "#":
						urlconf_name = nav_a_href[0:nav_a_href.find(".html")]
						url_1_2 = str(urlconf_name) + ".html"
						url_1_3 = urlconf_name.replace("-", "_")
						pattern = "url(r'^%s/$', 'canvas.views.navigation', {\"url\":\"%s\"}, name=\"%s\")," % (url_1_3, url_1_2, url_1_3)
			except:
				pass



# ==================================================#
#	Reload new copies of all the templates in the templates folder
# ==================================================#
class ReloadTemplates():
	def __init__(self):
		self.var = InitVariables()

	def reload(self):
		ans = pyautogui.confirm("Delete current template HTML files and reload original template HTML files from TEMPLATE_BACKUP_ZIP?")
		if ans == "OK":
			for file in self.var.TEMPLATE_FILES:
				filename, ext = os.path.splitext(file)
				if ext == ".html":
					try:
						os.remove(file)
					except Exception, e:
						print e
				else:
					print "There are no html files in your templates folder!"

			with zipfile.ZipFile(self.var.TEMPLATE_BACKUP_ZIP, "r") as z:
				z.extractall(self.var.TEMPLATE_FOLDER)

			try:
				shutil.rmtree(os.path.join(self.var.TEMPLATE_FOLDER,"__MACOSX"))
			except:
				pass


# ==================================================#
#	Main
# ==================================================#
# compile_templates = CompileStatic()
# compile_templates.loop()
src = "images/videos/explore.mp4"
yo = InitVariables()
yo.src_type(src)

# reload_templates = ReloadTemplates()
# reload_templates.reload()







