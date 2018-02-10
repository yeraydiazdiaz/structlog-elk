import logging

import structlog
import logstash


def configure_logging():
    structlog.configure(
        processors=[
            structlog.stdlib.filter_by_level,
            structlog.stdlib.add_log_level,
            structlog.stdlib.PositionalArgumentsFormatter(),
            structlog.processors.StackInfoRenderer(),
            structlog.processors.format_exc_info,
            structlog.processors.UnicodeDecoder(),
            # required as LogstashHandler uses `extra` for logging JSON values
            structlog.stdlib.render_to_log_kwargs,
        ],
        # required to mimic Flask's threadlocal context allowing
        # logging during the whole request process
        context_class=structlog.threadlocal.wrap_dict(dict),
        logger_factory=structlog.stdlib.LoggerFactory(),
        wrapper_class=structlog.stdlib.BoundLogger,
        cache_logger_on_first_use=True,
    )

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(
        structlog.stdlib.ProcessorFormatter(
            processor=structlog.dev.ConsoleRenderer())
    )

    app_logger = logging.getLogger('app')
    app_logger.addHandler(stream_handler)
    app_logger.setLevel(logging.INFO)

    # for TCP use TCPLogstashHandler and port 5000
    logstash_handler = logstash.LogstashHandler(
        'logstash', 5959, version=1)
    app_logger.addHandler(logstash_handler)
