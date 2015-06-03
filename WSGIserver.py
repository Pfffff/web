from paste import reloader
import selector
from jinja2 import Environment, FileSystemLoader

path_to_aboutme = """<a href="aboutme/aboutme.html">aboutme.html</a>"""
path_to_index = """<a href="index.html">index.html</a>"""

status_code = '200 OK'
headers = [('Content-Type','text/html; charset=UTF-8')]

# Базовый класс  
class Base(object):
    
    def __init__(self,environ,start_response,link,template):
    	# устанавливаем окружение
        self.env = environ
        # устанавливаем тело ответа
        self.start_response = start_response
        # получаем шаблоны при помощи loader, загрузчика шаблонов
        self.templates  = Environment(loader=FileSystemLoader('templates'))
        # устанавливаем шаблон
        self.template = template
        # устанавливаем ссылку
        self.link = link

    def __iter__(self):
    	# тело ответа содержит указанные ранее статус и заголовок
        self.start_response(status_code,headers)
        # загружаем шаблон с указанным названием
        template = self.templates.get_template(self.template)
        # вызываем метод render() объекта Template с контекстом, чтобы “выполнить” шаблон:
        yield template.render(link=self.link)
       
   
class Index(Base):

    def __init__(self,environ,start_response):
    	# передаём данные в конструктор базового класса
        Base.__init__(self, environ, start_response, path_to_index, "index.html")

class AboutMe(Base):
    def __init__(self,environ,start_responce):
    	# передаём данные в конструктор базового класса
        Base.__init__(self,environ,start_responce,path_to_aboutme,"aboutme.html")

def init():
    selector_ =  selector.Selector()
    # указываем пути и название классов-обработчиков
    selector_.add("/index.html",GET=Index) 
    selector_.add("/aboutme/aboutme.html",GET=AboutMe)
    # когда пути указаны, они становятся регулярными выражениями
    # когда selector_ получит запрос, он будет проверять его на соответствие с этими выражениями
    return selector_


if __name__=="__main__":
    from paste.httpserver import serve
    app = init()
    serve( app, host='localhost', port=8000)

