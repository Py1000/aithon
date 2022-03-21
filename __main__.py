import os
import termuxMain
from telethon import TelegramClient
from telethon.sessions import StringSession
from functions import *

import os


try:
    varFile = open("/storage/emulated/0/VARS/var.txt","r")
    varFile = varFile.read()
except:
    os.system("termux-setup-storage")
    os.mkdir("/storage/emulated/0/VARS")
    varFile = open("/storage/emulated/0/VARS/var.txt","a")
    API_ID = input("Enter API_ID: ")
    varFile.write(f"{API_ID} ")
    API_HASH = input("Enter API_HASH: ")
    varFile.write(f"{API_HASH} ")
    SESSION = input("Enter SESSION: ")
    varFile.write(f"{SESSION}")
    varFile = open("/storage/emulated/0/VARS/var.txt","r")
    varFile = varFile.read()
try:
    conFile = open("/storage/emulated/0/CONFIG/config.txt","r")
    conFile = conFile.read()
    conFileALIVE_TXT = open("/storage/emulated/0/CONFIG/ALIVE_TXT.txt")
    conFileALIVE_TXT = conFileALIVE_TXT.read()
except:
    os.system("termux-setup-storage")
    os.mkdir("/storage/emulated/0/CONFIG")
    conFile = open("/storage/emulated/0/CONFIG/config.txt", "w")
    conFileALIVE_TXT = open("/storage/emulated/0/CONFIG/ALIVE_TXT.txt","w")
    ALIVE_NAME = input("Enter ALIVE NAME [If you want to set this as default press enter]: ")
    ALIVE_TXT = input("Enter ALIVE TEXT [If you want to set this as default press enter]: ")
    ALIVE_PIC = input("Enter ALIVE PIC(link) [If you want to set this as default press enter]: ")
    if ALIVE_NAME == "":
     ccinFile.write("Owner ")
    else:
      conFile.writelines(f"{ALIVE_NAME} ")
    if ALIVE_TXT == "":
     conFileALIVE_TXT.write("Hey I am ALIVE!")
    else:
      conFileALIVE_TXT.writelines(ALIVE_TXT)
    if ALIVE_PIC == "":
     conFile.write("https://te.legra.ph/file/03c9b0143d1c222dede47.jpg")
    else:
      conFile.writelines(ALIVE_PIC)
    conFile = open("/storage/emulated/0/CONFIG/config.txt", "r")
    conFile = conFile.read()
    conFileALIVE_TXT = open("/storage/emulated/0/CONFIG/ALIVE_TXT.txt")
    conFileALIVE_TXT = conFileALIVE_TXT.read()

varFileS = varFile.split(" ")
API_ID = varFileS[0]
API_HASH = varFileS[1]
SESSION = varFileS[2]
session = str(SESSION)

user = TelegramClient(StringSession(session),API_ID,API_HASH)

user.start()
print("BOT ONLINE")
os.system("python /data/data/com.termux/files/home/aithon/termuxMain")
user.run_until_disconnected()
