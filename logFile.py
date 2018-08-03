import logging,logging.handlers

class my_log():
    def __init__(self):
        try:
            LOG_FileName =  "UpdateDB.log"
            self.logger = logging.getLogger('updatedb')
            self.logger.setLevel(logging.DEBUG)
            fh = logging.FileHandler(filename=LOG_FileName)
            fh.setLevel(logging.DEBUG)
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            fh.setFormatter(formatter)
            self.logger.addHandler(fh)
        except:
            print("exception in db log")

    def info(self ,  log_message):
        self.logger.info(log_message)


    def debug(self ,  log_message):
        self.logger.debug(log_message)


    def warning(self ,  log_message):
        self.logger.warning(log_message)


    def critical(self ,  log_message):
        self.logger.critical(log_message)


    def error(self ,  log_message):
        self.logger.error(log_message)
        
