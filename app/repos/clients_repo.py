import sqlalchemy as sa

from app.repos.abc_repo import AbstractRepo
from app.entities.client import Client
from app.tables.tbl_clients import tbl_clients


class ClientsRepo(AbstractRepo):
    entity_class = Client

    def __init__(self, postgresql_conn):
        self._conn = postgresql_conn

    @classmethod
    def _sa_clients(cls, filter_params=None):
        # here we can join addition tables if it's necessary
        return tbl_clients

    @classmethod
    def _project_clause(cls, project_params=None):
        # here we can map entity fields to tables columns
        # we also can take data from joined tables here
        visible_columns = project_params and project_params.attrs or None

        columns = {
            'id': tbl_clients.c.id,
            'is_enabled': tbl_clients.c.is_enabled,
            'created_at': tbl_clients.c.created_at,
            'updated_at': tbl_clients.c.updated_at,
            'name': tbl_clients.c.name,
            'country': tbl_clients.c.country,
            'city': tbl_clients.c.city,
        }

        clause = [
            column.label(column_label)
            for column_label, column in columns.items()
            if not visible_columns or column_label in visible_columns
        ]
        return clause

    @classmethod
    def _where_clause(cls, filter_params=None):
        clause = sa.and_(
            tbl_clients.c.is_enabled.is_(True)
        )

        if not filter_params:
            return clause

        if filter_params.id:
            clause = sa.and_(
                clause,
                tbl_clients.c.id == filter_params.id
            )
        elif filter_params.id__in:
            clause = sa.and_(
                clause,
                tbl_clients.c.id.in_(filter_params.id__in)
            )

        return clause

    @classmethod
    def _order_clause(cls, sorting_params=None):
        # here we can support additional sorting if it's necessary
        clause = (tbl_clients.c.id,)
        return clause

    async def get_count(self, filter_params=None):
        query = sa.select([
            sa.func.count(tbl_clients.c.id).label('count')
        ]).select_from(
            self._sa_clients(filter_params)
        ).where(
            self._where_clause(filter_params)
        )

        total_count = 0
        async for row in self._conn.execute(query, params=query.params):
            total_count = row['count']
            break

        return total_count

    async def get_list(self, filter_params=None, project_params=None,
                       sorting_params=None, slicing_params=None):
        query = sa.select(
            self._project_clause(project_params)
        ).select_from(
            self._sa_clients(filter_params)
        ).where(
            self._where_clause(filter_params)
        ).order_by(
            *self._order_clause(sorting_params)
        )

        if slicing_params:
            if slicing_params.limit is not None:
                query = query.limit(slicing_params.limit)
            if slicing_params.offset is not None:
                query = query.offset(slicing_params.offset)

        items_list = []
        async for row in self._conn.execute(query, params=query.params):
            item = self.entity_class(**row)
            items_list.append(item)

        return items_list

    async def create_list(self, items_list):
        await self._conn.execute(
            tbl_clients.insert(),
            [
                {
                    tbl_clients.c.id: item.id,
                    tbl_clients.c.is_enabled: True,
                    tbl_clients.c.created_at: item.created_at,
                    tbl_clients.c.updated_at: None,
                    tbl_clients.c.name: item.name,
                    tbl_clients.c.country: item.country,
                    tbl_clients.c.city: item.city,
                }
                for item in items_list
            ]
        )
        created_list = [self.entity_class(**item) for item in items_list]
        return created_list
