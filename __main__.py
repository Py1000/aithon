import os
import termuxMain
from telethon import TelegramClient
from functions import *

setup()
varFileS = varFile.split(" ")
API_ID = varFileS[0]
API_HASH = varFileS[1]
SESSION = varFileS[2]
session = str(SESSION)

user = TelegramClient("session",API_ID,API_HASH)
