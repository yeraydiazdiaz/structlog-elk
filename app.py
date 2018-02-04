from uuid import uuid4

from flask import Flask
import structlog

from log_config import configure_logging

app = Flask(__name__)
# should be called once on app initialisation
configure_logging()
logger = structlog.get_logger()


@app.route('/')
def root():
    # binds `request_id` to the current context
    log = logger.new(request_id=str(uuid4()))
    helper_function()
    log.info('an info', source='root')
    return 'Hello, world!'


def helper_function():
    # binds `helper_key: helper_value` to the current context
    logger.bind(helper_key='helper_value')
    # an event is logged with a message, optional keys as kwargs and context
    logger.warning('a warning', source='helper')


@app.errorhandler(Exception)
def base_error_handler(error):
    # exception logging includes traceback information
    logger.exception(error)
    return 'Woops, our bad, sorry!', 500


@app.route('/boom/')
def boom():
    log = logger.new(request_id=str(uuid4()))
    log.info('About to raise')
    raise Exception('Test exception')


if __name__ == '__main__':
    app.run()
