import platform
from dotenv import load_dotenv
import os
import logging
from simplify.hdb_connector import HDBConnector

def main():
    
    conn = HDBConnector().connect_to_hdb()  # Get connection class instance.
    get_machine_details(conn)
    logger.info("Program execution successful!!")

def get_machine_details(conn: object):
    cursor = conn.cursor()
    sql = "SELECT SYSTEM_ID, DATABASE_NAME, VERSION FROM M_DATABASE"
    cursor.execute(sql)
    result = cursor.fetchall()
    logger.info(f"Working on HANA system having SID {result[0][0]}, using database '{result[0][1]}' with version {result[0][2]} .")
    cursor.close()

if __name__ == "__main__":

    load_dotenv()   # Load environment variables from env file in app directory.

    #Initialize loggers with info level.
    logging.basicConfig()
    logger = logging.getLogger()
    log_level = os.getenv("logging_level")
    logger.setLevel(log_level)
    logger.info(f"Initialized all loggers to {logging.getLevelName(logger.getEffectiveLevel())} level.")

    # Verify the architecture of machine
    logger.debug("Running program on current platform architecture with" + platform.platform() 
    + platform.architecture()[0] + "operating system on top of" + platform.processor() + "platform.")

    main()