import os


__all__ = ['DefaultConfig']


class DefaultConfig:
    DEBUG = True
    POSTGRESQL_PROTOCOL = 'postgresql+psycopg2'
    POSTGRESQL_HOST = os.environ.get('POSTGRESQL_HOST', 'localhost')
    POSTGRESQL_PORT = os.environ.get('POSTGRESQL_PORT', '5432')
    POSTGRESQL_USERNAME = os.environ.get('POSTGRESQL_USERNAME', 'postgres')
    POSTGRESQL_PASSWORD = os.environ.get('POSTGRESQL_PASSWORD', '')
    POSTGRESQL_DB = os.environ.get('POSTGRESQL_DB', 'task23jul2019')

    @property
    def POSTGRESQL_URL(self):
        url = '{proto}://{username}:{password}@{host}:{port}/{db}'.format(
            proto=self.POSTGRESQL_PROTOCOL,
            host=self.POSTGRESQL_HOST,
            port=self.POSTGRESQL_PORT,
            username=self.POSTGRESQL_USERNAME,
            password=self.POSTGRESQL_PASSWORD,
            db=self.POSTGRESQL_DB)
        return url

    @property
    def ROOT_PATH(self):
        path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
        return path

    @property
    def TEMPLATES_PATH(self):
        path = os.path.join(self.ROOT_PATH, 'templates')
        return path
