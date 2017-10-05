from hashlib import md5

import asyncio
import aioredis
from aiohttp import web
import aiohttp_jinja2


async def redis_get(r, key):
    value = await r.get(key)
    return value

async def redis_set(r, key, value):
    await r.set(key, value)


@aiohttp_jinja2.template('index.html')
async def index(request):
    try:
        qparam = request.rel_url.query['hash']
        if qparam:
            flink = await redis_get(request.app['redis'], qparam)
            if flink:
                return web.HTTPTemporaryRedirect('http://'+flink)
    except:
        return {}

async def post_link(request):
    # wait for request
    data = await request.post()
    # calculate short link
    slink = md5(data['link'].encode('UTF-8')).hexdigest()[:8]
    # add link to db
    await redis_set(request.app['redis'], slink, data['link'])
    # return prepared link
    resp = 'http://localhost:8080/' + slink
    return web.Response(text=resp)

async def process_hash(request):
    path = request.match_info.get('hash', '')
    if path.startswith('hash='):
        path = path[5:13]
    resp = await redis_get(request.app['redis'], path)
    try:
        if not resp:
            raise ValueError
        return web.HTTPTemporaryRedirect('http://' + resp)
    except ValueError:
        resp = web.HTTPNotFound()
        resp.message = "there is no such link"
        return resp

def handle_404(request, message):
    response = aiohttp_jinja2.render_template('404.html',
                                              request,
                                              {'message' : message})
    return response