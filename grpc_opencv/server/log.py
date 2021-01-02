import logging
import logging.handlers
import os

LEVEL_MAP = {
    "CRITICAL": logging.CRITICAL,
    "ERROR": logging.ERROR,
    "WARNING": logging.WARNING,
    "INFO": logging.INFO,
    "DEBUG": logging.DEBUG,
    "NOTSET": logging.NOTSET,
}

def logging_error(trace_id, error_code, error_msg):
    logging.error("trace_id: {:}, error_code: {:}, {:}".format(trace_id, error_code, error_msg))

def init_logging(filename, verbose=False, level="INFO"):
    output_dir = os.path.dirname(filename)
    filename = os.path.basename(filename)

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    if not level.upper() in LEVEL_MAP:
        raise Exception("level {:} is not a valid logging level type and avilable choices: {:}".format(level, LEVEL_MAP.keys()))

    print("init_logging path: {:}, file: {:}, level: {:}".format(output_dir, filename, level))
    level = LEVEL_MAP[level.upper()]
    logger = logging.getLogger()
    logger.setLevel(level)

    # create formatter
    formatter = logging.Formatter('[%(asctime)s][%(filename)s:%(lineno)d][%(levelname)s]: %(message)s')

    if verbose: #and not logger.hasHandlers():
        handler = logging.StreamHandler()
        handler.setLevel(level)
        logger.addHandler(handler)

    #log/all
    handler = logging.handlers.RotatingFileHandler(os.path.join(output_dir, filename),
                                                 maxBytes=1024*1024*1024, backupCount=8, encoding='utf-8')
    handler.setLevel(level)
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    #log/error
    handler = logging.handlers.RotatingFileHandler(os.path.join(output_dir, 'error_{}'.format(filename)),
                                                   maxBytes=1024*1024*1024, backupCount=8, encoding='utf-8')
    handler.setLevel(logging.WARNING)
    handler.setFormatter(formatter)
    logger.addHandler(handler)


if __name__=="__main__":
    init_logging("log/server.log", verbose=True, level="INFO")


