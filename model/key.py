from lib.database import Database
import time

class Key:
    __conn = None
    __computerName = None
    __cursor = None

    def __init__(self, computerName, cfg_file):
        self.__conn = Database.connect(cfg_file);
        self.__computerName = computerName
        self.__cursor = self.__conn.cursor()

    def incrementKeyCount(self):
        try:
            sql = "INSERT INTO keylogger (keylogger.computer_name, keylogger.keys, keylogger.date) VALUES ('"+self.__computerName + "', 1, '" + time.strftime("%Y-%m-%d") + "') ON DUPLICATE KEY UPDATE keylogger.keys=keylogger.keys+1"
            self.__cursor.execute(sql)
        except:
            pass

    def __del__(self):
        self.__conn.close()
        self.__cursor.close()