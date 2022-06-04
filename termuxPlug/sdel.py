□sdel□

#
@admin_cmd()
async def sdel(event):
  message = event.raw_text
  sec = (message.split(" "))[1]
  to_show = (message.split("|"))[1]
  await event.edit(to_show)
  asyncio.sleep(int(sec))
  await event.delete()
