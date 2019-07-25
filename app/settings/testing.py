from .default import DefaultConfig


__all__ = ['TestingConfig']


class TestingConfig(DefaultConfig):
    POSTGRESQL_DB = 'task23jul2019_testing'
