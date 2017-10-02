import hashlib
from wsgiref.simple_server import make_server
from urllib.parse import parse_qs
from html import escape

import redis

from templates import t_index, t_404


def db_init(host, port):
    r = redis.StrictRedis(host, port)
    return r

def redis_add(db, value):
    try:
        key = hashlib.md5(value.encode('UTF-8')).hexdigest()[:8]
        db.set(key, value)
        print('Redis add: {} --> {}'.format(key, value))
        return key
    except:
        print("Can't evaluate hash")


def redis_get(db, key):
    try:
        value = db.get(key)
        return value
    except:
        print("Can't find the value")
        return None

def redirect_url(environ, start_response, to_url):
    status = '302 Temporary Redirect'
    response_headers = [
        ('Content-type', 'text/html'),
        ('Location', 'http://{}'.format(to_url))
    ]
    start_response(status, response_headers)
    return []

def app(environ, start_response):
    r = db_init('localhost', 6379)    
    try:
        response = r.client_list()
    except redis.ConnectionError:
        print("db hasn't found")

    path    = environ['PATH_INFO']
    method  = environ['REQUEST_METHOD']
    # POST request -> adding new link to db
    if method == 'POST':
        try:
            request_body_size = int(environ['CONTENT_LENGTH'])
            request_body = environ['wsgi.input'].read(request_body_size)
            request_body = request_body.decode('UTF-8')
        except (TypeError, ValueError):
            request_body = "0"
        dic = parse_qs(request_body)
        link = escape(dic.get('link', 'empty')[0])
        # link = escape(lk)
        resp = 'http://localhost:8080/'+redis_add(r, link) 
        # prepearing response
        status = "200 OK"
        headers = [('Content-type', 'text/plain')]
        start_response(status, headers)
        return [resp.encode('UTF-8')]

    elif method == 'GET':
        # if request has a query string -> link must have http://domainname/?hash=[short link]
        resp = ""
        qstring = environ['QUERY_STRING']
        if qstring != '':
            qlst = qstring.split('&')
            for arg in qlst:
                if arg.startswith('hash='):
                    resp = redis_get(r, arg[5:13])
                    if resp:
                        resp = resp.decode('UTF-8')
                    print('TYT -------> %s' % resp)
                print("param: %s" % arg)
                return redirect_url(environ, start_response, resp)
        else:
            # if path variable is / -> go to index page
            if path == '/':
                status = '200 OK'
                headers = [('Content-type', 'text/html')]
                start_response(status, headers)
                return[t_index.tindex.encode('UTF-8')]
            
            # path isn't empty -> check if it's value exists in db, if it is -> get needed link, otherwise -> 404
            splited_path = path.split('/')
            resp = redis_get(r, splited_path[-1])
            if resp:
                resp = resp.decode('UTF-8')
                print(resp)
                return redirect_url(environ, start_response, resp)
            
            else:
                status = '404 Not Found'
                headers = [('Content-type', 'text/html')]
                start_response(status, headers)
                return [t_404.t404.encode('UTF-8')]
        

if __name__ == '__main__':
    httpserv = make_server('localhost', 8080, app)
    httpserv.serve_forever()