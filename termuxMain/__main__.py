import os

os.system("cd")
os.system("cd aithon")

def load(plug):
  f = open(f"/data/data/com.termux/files/home/aithon/termuxPlug/{plug}.py","r")
  tep = f.split("#")
  print(tep)

load("hello")
