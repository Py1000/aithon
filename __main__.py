import os
import termuxMain
from telethon import TelegramClient
import functions import *

setup()
login()

user = TelegramClient("session",API_ID,API_HASH)
