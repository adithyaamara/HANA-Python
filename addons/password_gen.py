import random
import string
import logging
import os
from dotenv import load_dotenv
load_dotenv()
logger = logging.getLogger()
logger.setLevel(os.getenv("logging_level"))

class pwd_gen:
    def __init__(self):
        try:
            self._p_length = int(os.getenv("RandomPassLength"))
        except Exception as err:
            logger.critical("Missing Confiuration keys in .env 'RandomPassLength' !!!")
    def genarate(self):
        #-------password generator-------#
        lower = string.ascii_lowercase
        upper = string.ascii_uppercase
        num = string.digits
        all = lower + upper + num
        length = self._p_length
        temp = random.sample(all,length)
        randompass = "".join(temp)
        return randompass