import os

def setup():
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

