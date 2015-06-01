from paste import reloader
from webob import Request, Response

wikipedia = 'wikipedia.org'
httpbin = 'httpbin.org'


# №2
# имитируем запрос при помощи метода blank
wiki = Request.blank("wiki/Main_page") 

wiki.host = wikipedia
wiki.environ["SERVER_NAME"] = wikipedia
wiki.accept = "text/html"
wiki.user_agent = "User-Agent: Mozilla/5.0 (X11; U; Linux i686; ru; rv:1.9b5) Gecko/2008050509 Firefox/3.0b5"

# №3
# получение ip адреса
getIP = Request.blank("ip")
getIP.host = httpbin
getIP.environ["SERVER_NAME"] = httpbin
getIP.accept = '*/*'

# запрос, отправленный методом get
# получаем список параметров метода get
getRequest = Request.blank("get?foo=bar&1=2&2/0&error=True")
getRequest.host = httpbin
getRequest.environ["SERVER_NAME"] = httpbin
getRequest.accept = '*/*'

# запрос, отправленный методом post
# получаем список переданных параметров
postRequest = Request.blank("post")
postRequest.host = httpbin
postRequest.environ["SERVER_NAME"] = httpbin
postRequest.method = 'POST'
postRequest.content_length = 35
postRequest.content_type = "application/x-www-form-urlencoded"
postRequest.body = "foo=bar&1=2&2%2F0=&error=True"


# устанавливаем cookie
setCookie = Request.blank('cookies/set?country=Ru')
setCookie.host = httpbin
setCookie.environ["SERVER_NAME"] = httpbin
setCookie.accept = '*/*'
 
# получаем cookie
getCookies = Request.blank("cookies")
getCookies.host = httpbin
getCookies.environ["SERVER_NAME"] = httpbin
getCookies.accept = '*/*'
 
 
# в результате запроса получаем ссылку на перенаправление
redir = Request.blank('redirect/4')
redir.host = httpbin
redir.environ["SERVER_NAME"] = httpbin
redir.accept = '*/*'
 
 
# задание 4
# информацию, отправленная с помощью метода post
# получаем ответ в виде списка переданных параметров
postReq = Request.blank("post")
postReq.host = httpbin
postReq.environ["SERVER_NAME"] = httpbin
postReq.method = 'POST'
post_body = "firstname=Alex&lastname=Macedonian&group=fo321001&message=helloWorld"
postReq.content_length = len(post_body)
postReq.content_type = "application/x-www-form-urlencoded"
postReq.body = post_body
 
 
requests = [wiki,getIP,getRequest,postRequest,setCookie,getCookies,redir,postReq]
 
i=0
for request in requests:
    res = request.get_response()
    f = open(request.host+str(i)+".html",'w')
    f.write(res.body)
    f.close();
    i=i+1
