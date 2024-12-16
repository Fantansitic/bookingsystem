import os

env_name = os.getenv('RUN_ENV', 'dev')

if env_name == 'production':
    from .production import *
else:
    from .dev import *