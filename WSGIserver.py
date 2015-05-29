from paste import reloader
from paste.httpserver import serve

import selector 
from jinja2 import Environment, FileSystemLoader

status = '200 OK'
HTTPheader = [('Content-Type', 'text/html; charset=UTF-8')]
link_aboutme = """<a href="about/about.html">link to aboutme.html</a>"""
link_index = """<a href="../index.html">link to index.html</a>"""


TOP = "<div class='top'>Middleware TOP</div>"
BOTTOM = "<div class='botton'>Middleware BOTTOM</div>"

class BaseApp(object):
	def __init__(self, environ, start_response,link,template):
		self.env = environ
		self.start_response = start_response
		self.templates = Environment(loader=FileSystemLoader('templates'))
		self.template = templateself.link = link

	def __iter__(self):
		self.start_response(status,HTTPheader)
		template = self.templates.get_template(self.template)
		yield template.render(link = self.link)


class Index(BaseApp):
	def __init__(self,environ,start_response):
		BaseApp.__init__(self,environ,start_response,link_aboutme,"index.html")

class Aboutme(BaseApp):
	def __init__(self,environ,start_response):
		BaseApp.__init__(self,environ,start_response,link_index,"about.html")
		
def init():
    disp =  selector.Selector()
    disp.add("/index.html",GET=IndexApp)
    disp.add("/about/about.html",GET=AboutApp)
    return disp

def check_true():
        res = True
        for i in xrange(100):
            if i > i+1:
                res = init()
        return res

if __name__=="__main__":
    from paste.httpserver import serve
    if check_true():
        raise Exception("error")
    app = init()
    serve( app, host='localhost', port=8000)