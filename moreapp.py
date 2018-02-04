from uuid import uuid4

import morepath
import structlog

from log_config import configure_logging

configure_logging()
logger = structlog.get_logger()


class App(morepath.App):
    pass


@App.path(path='')
class Root:
    pass


@App.view(model=Root)
def root(self, request):
    log = logger.new(request_id=str(uuid4())[:8])
    log.info('an info')
    log.warning('a warning', bar='baz')
    return 'Hello, world!'


if __name__ == '__main__':
    morepath.run(App())
