import os, sys, unicodedata
from model.key import Key
from model.word import Word
if os.name == 'posix':
    from pynput import keyboard

from pprint import pprint

class KeyPressCtrl:
    __computerName = None
    __keyModel = None
    __wordModel = None
    __lastword = None

    def keyPressEvent(self, event):
        try:
            if os.name == 'nt':
                # win version
                keyid = event.KeyID
                keychar = chr(event.Ascii)

                if keyid == 32 or keyid == 13:
                    if self.__lastword.strip(" ") != "":
                        self.__wordModel.incrementWordCount()
                    self.__keyModel.incrementKeyCount()
                    self.__lastword = ""
                else:
                    self.__lastword = self.__lastword + str(keychar)
                    self.__keyModel.incrementKeyCount()

                return True;
            else:
                # mac version
                try:
                    if event == keyboard.Key.space or event == keyboard.Key.enter:
                        if self.__lastword.strip(" ") != "":
                            self.__wordModel.incrementWordCount()
                        self.__keyModel.incrementKeyCount()
                        self.__lastword = ""
                    elif str(event).find("Key") == -1:
                        self.__lastword = self.__lastword + str(event)[-2:-1]
                        self.__keyModel.incrementKeyCount()
                    else:
                        self.__keyModel.incrementKeyCount()
                except AttributeError:
                    self.__keyModel.incrementKeyCount()
                    pass
        except:
            pass

    def __init__(self, computerName):
        self.__computerName = computerName
        self.__keyModel = Key(self.__computerName)
        self.__wordModel = Word(self.__computerName)
        self.__lastword = ""

        if os.name == 'nt':
            import pyHook, pythoncom

            try:
                hooks_manager = pyHook.HookManager()
                hooks_manager.KeyDown = self.keyPressEvent
                hooks_manager.HookKeyboard()
                pythoncom.PumpMessages()
            except:
                pass
        elif os.name == 'posix':
            try:
                with keyboard.Listener(on_press=self.keyPressEvent) as listener:
                    try:
                        listener.join()
                    except:
                        pass


            except:
                pass
        else:
            sys.exit("# Operating system ("+os.name+") not supported!")
