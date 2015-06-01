from paste import reloader
import selector
from jinja2 import Environment, FileSystemLoader

path_to_aboutme = """<a href="aboutme/aboutme.html">aboutme.html</a>"""
path_to_index = """<a href="index.html">index.html</a>"""

status_code = '200 OK'
headers = [('Content-Type','text/html; charset=UTF-8')]

class Base(object):

    def __init__(self,environ,start_response,link,template):
        self.env = environ
        self.start_response = start_response
        self.templates  = Environment(loader=FileSystemLoader('templates'))
        self.template = template
        self.link = link

    def __iter__(self):
        self.start_response(status_code,headers)
        template = self.templates.get_template(self.template)
        yield template.render(link=self.link)
             
class Index(Base):
    def __init__(self,environ,start_response):
        Base.__init__(self, environ, start_response, path_to_index, "index.html")

class AboutMe(Base):
    def __init__(self,environ,start_responce):
        Base.__init__(self,environ,start_responce,path_to_aboutme,"aboutme.html")

def init():
    selector_ =  selector.Selector()
    selector_.add("/index.html",GET=Index)
    selector_.add("/aboutme/aboutme.html",GET=AboutMe)
    return selector_


if __name__=="__main__":
    from paste.httpserver import serve
    app = init()
    serve( app, host='localhost', port=8000)

