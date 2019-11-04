import os
from .settings import root

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': (
                    '%(asctime)s [%(process)d] [%(levelname)s] %(message)s ' +
                    'pathname=%(pathname)s lineno=%(lineno)s funcname=%(funcName)s'
            ),
            'datefmt': '%Y-%m-%d %H:%M:%S',
        },
        'simple': {
            'format': '%(asctime)s [%(levelname)s] %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S',
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        },
        'console-app': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'formatter': 'simple',
            'filename': os.path.join(root.root, 'logs', 'web', 'console-app.log')
        },
        'console-verbose': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'formatter': 'verbose',
            'filename': os.path.join(root.root, 'logs', 'web', 'console-verbose.log')
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console', 'console-app'],
            'level': 'INFO',
            'propagate': True,
        },
        'security': {
            'handlers': ['console-verbose'],
            'level': 'ERROR',
            'propagate': False,
        },
    },

}
