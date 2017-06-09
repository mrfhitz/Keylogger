from controller.keyPressCtrl import KeyPressCtrl
import sys, os

if len(sys.argv) > 2:
    name = str(sys.argv[1])
    cfg_file = str(sys.argv[2])
elif len(sys.argv) > 1:
    name = str(sys.argv[1])
    cfg_file = str(os.path.dirname(os.path.abspath(sys.modules['__main__'].__file__)) + "/keylogger.ini")
else:
    name = "DEFAULT"
    cfg_file = str(os.path.dirname(os.path.abspath(sys.modules['__main__'].__file__)) + "/keylogger.ini")

keypress = KeyPressCtrl(name, cfg_file)
