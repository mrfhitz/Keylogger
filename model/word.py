from lib.database import Database
import time

class Word:
    __conn = None
    __computerName = None
    __cursor = None

    def __init__(self, computerName):
        self.__conn = Database.connect();
        self.__computerName = computerName
        self.__cursor = self.__conn.cursor()

    def incrementWordCount(self):
        try:
            sql = "INSERT INTO keylogger (keylogger.computer_name, keylogger.words, keylogger.date) VALUES ('"+self.__computerName + "', 1, '" + time.strftime("%Y-%m-%d") + "') ON DUPLICATE KEY UPDATE keylogger.words=keylogger.words+1"
            self.__cursor.execute(sql)
        except:
            pass

    def __del__(self):
        self.__conn.close()
        self.__cursor.close()