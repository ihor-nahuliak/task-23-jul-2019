import sys
import os

from migrate.versioning.shell import main


if __name__ == '__main__':
    APP_PATH = os.path.abspath(os.path.join(__file__, os.pardir, os.pardir))
    ROOT_PATH = os.path.abspath(os.path.join(APP_PATH, os.pardir))
    sys.path.append(APP_PATH)
    sys.path.append(ROOT_PATH)

    from quicksets import settings

    main(repository=os.path.join(APP_PATH, 'migrations'),
         url=settings.POSTGRESQL_URL, debug=settings.DEBUG)
