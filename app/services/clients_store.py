from app.services.abstract_store import AbstractStore
from app.repos.clients_repo import ClientsRepo


class ClientsStore(AbstractStore):
    repo_class = ClientsRepo
