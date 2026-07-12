
import structlog
import logging
import sys
import os
# from client import thread_id_str           
from logging.handlers import RotatingFileHandler
from datetime import datetime

# log = structlog.get_logger()
#                 log.error(
#                     type(e).__name__,
#                     message = str(e)
                        
                    
#                 )
#                 logger 
                
                
def setup_logging(log_level: str = "INFO", log_dir: str = "logs"):
    #log directory
    os.makedirs(log_dir, exist_ok=True)
    #timestamped log filename
    log_file = os.path.join(
        log_dir,
        f"app_{datetime.now().strftime('%Y-%m-%d___%H-%M-%S')}"
    )
    #file handler: 10 mb max per file, keep 5 backups = 60 MB total max
    file_handler = RotatingFileHandler(
        log_file,
        maxBytes=10 * 1024 * 1024,
        backupCount=5
    )
    #setting up formatter so the raw message only get logs - log file handler format
    file_handler.setFormatter(logging.Formatter('%(message)s'))
    #conosle format handler - message handling in console
    stream_handler = logging.StreamHandler(sys.stdout)
    stream_handler.setFormatter(logging.Formatter('%(message)s'))
    #configure root logger
    root_logger = logging.getLogger(__name__)
    #using getattr to get a set level ex - DEBUG, INFO so .upper()
    root_logger.setLevel(getattr(logging, log_level.upper()))
    #Remove existing handlers to avoid duplicated if called more than once
    for handler in root_logger.handlers[:]:
        root_logger.removeHandler(handler)
    root_logger.addHandler(file_handler)
    root_logger.addHandler(stream_handler)
    #configure structlog
    structlog.configure(
        processors=[
            structlog.contextvars.merge_contextvars,
            structlog.processors.CallsiteParameterAdder,
            structlog.processors.add_log_level,
            structlog.processors.TimeStamper(fmt='iso'),
            structlog.processors.StackInfoRenderer,
            #Formats it to a flat string like the standard library would on the console.
            structlog.processors.format_exc_info,
            structlog.processors.JSONRenderer()
        ],
        wrapper_class=structlog.stdlib.BoundLogger,
        context_class=dict,
        logger_factory = structlog.stdlib.LoggerFactory(),
        cache_logger_on_first_user=True,
    )
    
def get_logger(name: str) -> structlog.BoundLogger:
    return structlog.get_logger(name)


