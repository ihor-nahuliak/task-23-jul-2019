from aiohttp import web


__all__ = ['middlewares']



@web.middleware
async def todo_middleware(request, handler):
    # TODO: do something
    response = await handler(request)
    return response


middlewares = []
