import os

os.system("cd")
os.system("cd aithon")


def load(plug):
  f = open(f"/data/data/com.termux/files/home/aithon/termuxPlug/{plug}.py","r")
  rawCode = f.read()
  rawCodeS = rawCode.split("□")
  cmd = rawCodeS[1]
  mainCode = rawCode.split("#")
  codes = mainCode[1]
  cmdLine = codes.replace("@admin_cmd()",f"@user.on(events.NewMessage(pattern=".{cmd}",outgoing = True))")
  os.mkdir("/data/data/com.termux/files/home/aithon/termuxOp")
  mFile = open("/data/data/com.termux/files/home/aithon/termuxOp/__main__.py","a")
  mfile.write(f"")
  

load("hello")
