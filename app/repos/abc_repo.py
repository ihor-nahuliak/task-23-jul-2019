import abc
from types import SimpleNamespace as bunch


class AbstractRepo(metaclass=abc.ABCMeta):
    entity_class = NotImplemented

    @abc.abstractmethod
    async def get_count(self, filter_params=None):
        return 0

    @abc.abstractmethod
    async def get_list(self, filter_params=None, project_params=None,
                       sorting_params=None, slicing_params=None):
        return []

    async def get_item(self, filter_params):
        items_list = await self.get_list(
            filter_params=filter_params,
            slicing_params=bunch(offset=0, limit=1))
        item = items_list[0] if items_list else None
        return item

    @abc.abstractmethod
    async def create_list(self, items_list):
        return []

    @abc.abstractmethod
    async def create_item(self, item):
        created_item = await self.create_list(items_list=[item])
        return created_item

    @abc.abstractmethod
    async def update_list(self, items_list):
        return []

    @abc.abstractmethod
    async def update_item(self, item):
        updated_item = await self.update_list(items_list=[item])
        return updated_item

    @abc.abstractmethod
    async def delete_list(self, filter_params):
        pass
