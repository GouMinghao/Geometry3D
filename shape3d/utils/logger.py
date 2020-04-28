import logging
from logging.config import dictConfig

log_level = logging.WARNING
logging_config = dict(
    version=1,
    formatters={
        'f':
        {
            'format': '%(asctime)s [shape3d %(levelname)s] %(message)s'
        },
    },
    handlers={
        'h':
        {
            'class': 'logging.StreamHandler',
            'formatter': 'f',
            'level': log_level
        }
    },
    root={
        'handlers': ['h'],
        'level': log_level
    },
)
dictConfig(logging_config)
main_logger = logging.getLogger()


def set_log_level(level='WARNING'):
    """setup the log level for the logger"""
    global log_level, main_logger
    if level == 'DEBUG':
        log_level = logging.DEBUG
    elif level == 'INFO':
        log_level = logging.INFO
    elif level == 'WARNING':
        log_level = logging.WARNING
    elif level == 'ERROR':
        log_level = logging.ERROR
    elif level == 'CRITICAL':
        log_level = logging.CRITICAL
    else:
        raise ValueError("Unknown log level %s, which should one of 'DEBUG','INFO','WARNING','ERROR','CRITICAL'" % (log_level,))
    change_main_logger()


def change_main_logger():
    global main_logger, log_level
    logging_config = dict(
        version=1,
        formatters={
            'f':
            {
                'format': '%(asctime)s [shape3d %(levelname)s] %(message)s'
            },
        },
        handlers={
            'h':
            {
                'class': 'logging.StreamHandler',
                'formatter': 'f',
                'level': log_level
            }
        },
        root={
            'handlers': ['h'],
            'level': log_level
        },
    )
    dictConfig(logging_config)
    main_logger = logging.getLogger()

def get_main_logger():
    global main_logger
    return main_logger
