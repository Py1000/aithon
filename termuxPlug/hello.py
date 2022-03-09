import tele
user = "YK"

@admin_cmd(pattern=".hello")
async def hello(event):
  await event.edit("Hello!")
