□spam□

#
@admin_cmd()
async def spam(event):
  id = event.chat_id
  raw = event.raw_text.split(" ")
  try:
    spamCount = raw[1]
  except:
    await event.edit("**ERROR OCCURRED \n Do :** ```.spam <number> | <spam Message>``` ")
  try:
    spamCount = int(spamCount)
  except:
    await event.edit("**ERROR OCCURRED \n Do :** ```.spam <number> | <spam Message>``` ")
    reboot()
  rawOp = event.raw_text.split("|")
  try:
    spamMessage = rawOp[1]
  except:
    await event.edit("**ERROR OCCURRED \n Do :** ```.spam <number> | <spam Message>``` ")
    reboot()
  i = 0
  while i != spamCount:
    await user.send_message(id,spamMessage)
    i = i+1
  print(f"\nCommand Used : spam \nLocation : {id} \n")
