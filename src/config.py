

import os
import yaml
import logging.config
import logging


def setup_logging(path='logging.yaml', log_level=logging.INFO):
    if os.path.exists(path):
        with open(path, 'rt') as f:
            try:
                config = yaml.safe_load(f.read())
                logging.config.dictConfig(config)
            except Exception as e:
                print(e)
                print('Error in Logging Configuration. Using default configs')
                logging.basicConfig(level=log_level)
    else:
        print('Failed to load configuration file. Using default configs')
        logging.basicConfig(level=log_level)
