from .default import DefaultConfig


__all__ = ['DevelopConfig']


class DevelopConfig(DefaultConfig):
    POSTGRESQL_DB = 'task23jul2019_develop'
