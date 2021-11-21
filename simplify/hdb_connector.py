from hdbcli import dbapi    # hana client library for python
from dotenv import load_dotenv
import logging
import os
logger = logging.getLogger()
load_dotenv()

class HDBConnector:
    def __init__(self) -> None:
        #Initialize HDB connection
        try:
            self._address=os.getenv("endpoint")
            self._port=os.getenv("port")
            self._user=os.getenv("user")
            self._password=os.getenv("pwd")
        except:
            logger.critical("Please define environment variable in .env file.")
            exit()
    
    def connect_to_hdb(self):
        try:
            conn = dbapi.connect(self._address, self._port, self._user, self._password, 
                #Additional parameters
                encrypt=True, # must be set to True when connecting to HANA as a Service
                sslValidateCertificate=True
            )
            logger.info(f'Successfully acquired connection to hana endpoint "{self._address}" over port {self._port}. \n Logged in User -> {self._user}')
            return conn
        except Exception as err:
            logger.critical("Connection Failure : ",err)
            exit()
 