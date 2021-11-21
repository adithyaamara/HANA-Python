from hdbcli import dbapi    # hana client library for python
from dotenv import load_dotenv
import logging
import os
load_dotenv()
logger = logging.getLogger()
logger.setLevel(os.getenv("logging_level"))
class HDBConnector():
    def __init__(self) -> None:
        #Initialize HDB connection
        try:
            self._address=os.getenv("endpoint")
            self._port=os.getenv("port")
            self._user=os.getenv("user")
            self._password=os.getenv("pwd")
            try:
                self._conn = dbapi.connect(self._address, self._port, self._user, self._password, 
                    #Additional parameters
                    encrypt=True, # must be set to True when connecting to HANA as a Service
                    sslValidateCertificate=True
                )
                logger.info(f'Successfully acquired connection to hana endpoint "{self._address}" over port {self._port}. \n Logged in User -> {self._user}')
            except Exception as err:
                logger.critical("Connection Failure : ",err)
                exit()
        except:
            logger.critical("Please define environment variable in .env file.")
            exit()
    
    def db_transaction(self,query:str,rec_count,commit_req:bool):
        try:
            cursor = self._conn.cursor()
            logger.debug("DB CONNECTION SUCCESSFUL!!!!!!!!")
        except Exception as e:
            logger.critical("HANA Connection error : ",e)
            return "conn_err"
        cursor.execute(query)
        if commit_req == True:
            self._conn.commit()  #Commiting the sql state and returning null because insert statements don't return any records.
            return None
        if rec_count == 1:
            result = cursor.fetchone()
            cursor.close()
            return result
        else:
            result = cursor.fetchall()
            cursor.close()
            return result
 