import os

os.system("cd")
os.system("cd aithon")


def load(plug):
  f = open(f"/data/data/com.termux/files/home/aithon/termuxPlug/{plug}.py","r")
  rawCode = f.read()
  rawCodeS = rawCode.split("□")
  cmd = rawCodeS[1]
  nCmd = f".{cmd}"
  mainCode = rawCode.split("#")
  codes = mainCode[1]
  cmdLine = codes.replace("@admin_cmd()",f"@user.on(events.NewMessage(pattern='{nCmd}',outgoing=True))")
  mFile = open("/data/data/com.termux/files/home/aithon/termuxOp/__main__.py","a")
  mFile.write(f"\n\n\n {cmdLine}")
  print(f"Plugin Loaded : {plug}")
  
os.system("clear")
print("《BOT LOG》")

load("rhi")
load("del")
load("ehi")
load("spam")

fileOp = open("/data/data/com.termux/files/home/aithon/termuxOp/__main__.py","a")
fileOp.write("user.run_until_disconnected()")
