import logging
from logging.config import dictConfig
logging_config = dict(
    version=1,
    formatters=
    {
        'f':
        {
            'format':'%(asctime)s %(name)-5s %(levelname)-9s%(message)s'
        },
        'f1':
        {
            'format':'%(asctime)s %(name)-5s %(levelname)-10s%(message)s'
        }
    },
    handlers={
        'h': 
        {
            'class': 'logging.StreamHandler',
            'formatter': 'f',
            'level': logging.DEBUG
        }
        # },
        # 'h1':
        # {
        #     'class': 'logging.StreamHandler',
        #     'formatter': 'f1',
        #     'level': logging.INFO
        # }
    },
    root=
    {
        'handlers': ['h'],
        'level': logging.DEBUG,
    },
)

dictConfig(logging_config)
logger = logging.getLogger()
logger.warning("this is warning")
logger.debug("This is debug logging")
logger.error("This is error")
logger.critical("this is critical")
logger.info("This is Info")