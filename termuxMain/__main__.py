import os

os.system("cd")
os.system("cd aithon")

def load(plug):
  f = open(f"/data/data/com.termux/files/home/aithon/termuxPlug/{plug}.py","r")
  rawCode = f.read()
  rawCodeS = rawCode.split("□")
  cmd = rawCodeS[1]
  mainCode = rawCode.split("#")
  print(mainCode)

load("hello")
