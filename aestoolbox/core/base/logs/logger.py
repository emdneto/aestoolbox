"""AES-Toolbox Basic Logger Module"""

import logging
from logging import config, getLogger


LOG = getLogger(__name__)

class ToolboxLogger:
    
    @staticmethod
    def loadConfig(config_file, debug=False):
        try:
            config.fileConfig(config_file, disable_existing_loggers=False)
            LOG.info('Logging configuration file loaded successfully!')
        except Exception as err:
            LOG.warning('Failed to load Logging configuration file. %s', err)
            
        if debug:
            LOG.info('Enabling DEBUG Logging mode')
            level = logging.DEBUG
            logger = getLogger('feta')
            logger.setLevel(level)
            for handler in logger.handlers:
                handler.setLevel(level)
            LOG.info('DEBUG Logging mode was enabled successfully!')
            
        
        
        


