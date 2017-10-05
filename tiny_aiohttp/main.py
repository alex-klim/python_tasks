from aiohttp import web
import aiohttp_jinja2
import jinja2
import asyncio

from views import *


async def get_app():

    async def static_processor(request):
        return {'STATIC_URL': '/static/'}

    async def error_middleware(app, handler):
        async def middleware_handler(request):
            try:
                response = await handler(request)
                if response.status == 404:
                    return handle_404(request, response.message)
                return response
            except web.HTTPException as ex:
                if ex.status == 404:
                    return handle_404(request, ex.reason)
                raise
        return middleware_handler

    app = web.Application(middlewares=[error_middleware])

    app.router.add_post('/', post_link)
    app.router.add_get('/', index)
    app.router.add_get('/{hash}', process_hash)
    app.router.add_static('/static', 'static')

    aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader('templates/'),
                                    context_processors=[static_processor])

    app['redis'] = await aioredis.create_redis(('localhost', 6379),
                                               db=1, encoding='utf-8')

    async def close_redis(app):
        print('closing redis\n')
        app['redis'].close()

    app.on_cleanup.append(close_redis)

    return app

loop = asyncio.get_event_loop()
app = loop.run_until_complete(get_app())
web.run_app(app, host='localhost', port=8080)