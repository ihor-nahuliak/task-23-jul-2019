from .default import DefaultConfig


__all__ = ['ProductConfig']


class ProductConfig(DefaultConfig):
    DEBUG = False
    POSTGRESQL_DB = 'task23jul2019_product'
