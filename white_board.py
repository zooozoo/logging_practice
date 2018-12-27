import logging

rootlogger = logging.getLogger()
rootlogger.setLevel(logging.INFO)
stream_handler = logging.StreamHandler()
rootlogger.addHandler(stream_handler)

mylogger = logging.getLogger('my')
mylogger.setLevel(logging.INFO)
stream_handler2 = logging.StreamHandler()
mylogger.addHandler(stream_handler2)
mylogger.propagate = 0

mylogger.info('message from mylogger')
