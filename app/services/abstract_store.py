import abc

import asyncio

from app.repos.abc_repo import AbstractRepo


class AbstractStore(metaclass=abc.ABCMeta):
    repo_class = AbstractRepo

    def __init__(self):
        self.__repo = None

    @property
    def _repo(self):
        # lazy property (loop must exist at the call moment)
        if not self.__repo:
            loop = asyncio.get_event_loop()
            self._repo = self.repo_class(postgresql_conn=loop.postgresql_conn)
        return self._repo

    async def get_count(self, filter_params=None):
        total_count = await self._repo.get_count(filter_params=filter_params)
        return total_count

    async def get_list(self, filter_params=None, project_params=None,
                       sorting_params=None, slicing_params=None):
        items_list = await self._repo.get_list(filter_params=filter_params,
                                               project_params=project_params,
                                               sorting_params=sorting_params,
                                               slicing_params=slicing_params)
        return items_list

    async def get_item(self, filter_params):
        item = await self._repo.get_item(filter_params=filter_params)
        return item

    async def create_list(self, items_list):
        created_list = await self._repo.create_list(items_list)
        return created_list

    async def create_item(self, item):
        created_item = await self._repo.create_item(item=item)
        return created_item

    async def update_list(self, items_list):
        updated_list = await self._repo.update_list(items_list)
        return updated_list

    async def update_item(self, item):
        updated_item = await self._repo.update_item(item=item)
        return updated_item

    async def delete_list(self, filter_params):
        await self._repo.delete_list(filter_params=filter_params)
