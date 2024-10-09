from SignLanguage.logger import logging
from SignLanguage.exception import SignException
import sys



#logging.info('welcome to the object detection project')

try: 
    a = 7/"0"


except Exception as e:
    raise SignException(e,sys) from e