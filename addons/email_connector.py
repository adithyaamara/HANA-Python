import smtplib, ssl
import logging
from dotenv import load_dotenv
import os
load_dotenv()
logger = logging.getLogger()
logger.setLevel(os.getenv("logging_level"))

class email_conn:
    def __init__(self):
        try:
            self._mail_server = os.getenv("MAIL_SERVER")
            self._mailport = os.getenv("MAIL_PORT")
            self._mail_sender = os.getenv("MAIL_USERNAME")
            self._mailpasswrord = os.getenv("MAIL_PASSWORD")
            self._context = ssl.create_default_context()
            logger.info("------------------Extracted all required env vars!!!!--------------------")
        except Exception as e:
            logger.critical("Missing configuration!!!!! Please ensure to use proper .env file.")
            exit(e)
        self._server = smtplib.SMTP_SSL(self._mail_server, self._mailport, context=self._context)
        try:
            logger.info("----------Trying to Authenticate--------------")
            self._server.login(self._mail_sender , self._mailpasswrord)
            logger.info("Authenticated with SMTP Server successfully...")
        except Exception as err:
            logger.critical(f"Authntication Failed !!, {err}")
            exit()   
    
    def send_mail(self,subject:str,msg_body:str,recipients):
        message = 'Subject: {}\n\n{}'.format(subject, msg_body)     # Build the EMAIL to be sent.
        try:
            self._server.sendmail(self._mail_sender, recipients, message)
            return "success"
        except Exception as err:
            logger.critical(err)
            logger.critical("Error in email service....")
            return None
