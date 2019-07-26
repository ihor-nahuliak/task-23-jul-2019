from aiohttp import web
from aiohttp_jinja2 import render_template

from app.utils import JsonResponse
from app.services.abstract_store import AbstractStore


__all__ = ['routes']


routes = web.RouteTableDef()


@routes.get('/')
@routes.get('/index.html')
async def index_page(request):
    return render_template('index.html', request, {})


class AbstractStoreView(web.View):
    filter_schema_class = None
    project_schema_class = None
    sorting_schema_class = None
    slicing_schema_class = SlicingSchema
    result_schema_class = NotImplemented
    service_class = AbstractStore

    async def get(self):
        params = {}
        params.update(dict(self.request.match_info))
        params.update(dict(self.request.query))

        if self.filter_schema_class:
            filter_schema = self.filter_schema_class(strict=True)
            filter_params, _ = filter_schema.load(params)
        else:
            filter_params = None

        if self.project_schema_class:
            project_schema = self.project_schema_class(strict=True)
            project_params, _ = project_schema.load(params)
        else:
            project_params = None

        if self.sorting_schema_class:
            sorting_schema = self.sorting_schema_class(strict=True)
            sorting_params, _ = sorting_schema.load(params)
        else:
            sorting_params = None

        if self.slicing_schema_class:
            slicing_schema = self.slicing_schema_class(strict=True)
            slicing_params, _ = slicing_schema.load(params)
        else:
            slicing_params = None

        service = self.service_class()

        total_count = await service.get_count(filter_params=filter_params)
        items_list = await service.get_list(filter_params=filter_params,
                                            project_params=project_params,
                                            sorting_params=sorting_params,
                                            slicing_params=slicing_params)

        result_schema = self.result_schema_class(strict=True)
        result, _ = result_schema.dump(items_list, many=False)

        return JsonResponse(items_list, status=200)


@routes.view('/api/v1/clients')
@routes.view('/api/v1/clients/{id}')
class ClientsView(AbstractStoreView):
    filter_schema_class = ClientsFilterSchema
    result_schema_class = ClientsResultSchema
    service_class = ClientsStore
