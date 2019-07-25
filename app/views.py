from aiohttp import web
from aiohttp_jinja2 import render_template


__all__ = ['routes']


routes = web.RouteTableDef()


@routes.get('/')
@routes.get('/index.html')
async def index_page(request):
    return render_template('index.html', request, {})
