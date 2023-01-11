"""Logger Module"""
import logging

if __name__ == '__main__':
    log_level = logging.WARNING
    logging_config = dict(
        version=1,
        formatters={
            'f':
            {
                'format': '%(asctime)s [Geometry3D %(levelname)s] %(message)s'
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
    logging.config.dictConfig(logging_config)

main_logger = logging.getLogger(__name__)

def set_log_level(level):
    main_logger.setLevel(level)

def get_main_logger():
    '''
    **Input:**

    No Input

    **Output:**

    main_logger: The logger instance
    '''
    return main_logger
