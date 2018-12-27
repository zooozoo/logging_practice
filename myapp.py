import logging

rootlogger = logging.getLogger()
rootlogger.setLevel(logging.INFO)
stream_handler = logging.StreamHandler()
rootlogger.addHandler(stream_handler)
