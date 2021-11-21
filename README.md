# hanaapp

A python project on demonstrating capabilities of hana programmatic access using hdbcli.

# Config Required : 

 - A ".env" file like below is to be present in app directory, Please edit the default fields and give only one value per column.
 ```text
    # db config
    user = hana_database_username
    pwd = password_please
    endpoint = url_or_sql_endpoint_of_hana_system_here
    port = port_on_which_hana_is_exposed
    # logging config
    logging_level = INFO | DEBUG
    # email service config
    MAIL_PASSWORD = mail_password_here
    MAIL_SERVER = smtp.gmail.com
    MAIL_PORT = 465
    MAIL_USERNAME = YOUR_EMIAL_ID@gmail.com
    # password generator config
    RandomPassLength = 10   # Any int
    # Base flask app server config.
    App_Interface = 127.0.0.1 | 0.0.0.1
    App_Port = 4444   # Any port 
    APP_SECRET = XXXXXXXXXXXXXXX    # aNY STRING.
 ```  

- A HANA DATABASE with all commands listed in `required_sql.sql` executed.

# Usage :
- Install dependencies using `pip install -r requirements.txt`
- **NO GUI Simple App** -> `python -m main.py` -- Limited, admin funcionality. UNDER DEVELOPMENT!!!!!
- **With GUI** -> `python -m gui-main.py` and navigate to `http://localhost:4444` in chrome.

# Closing Notes:
 - Flask Application and UI reused from my another repo. [Find it here](https://github.com/adithyaamara/FlaskApp.git)