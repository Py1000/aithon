□spam□

#
@admin_cmd()
async def spam():
  @user.on(events.NewMessage(pattern="\.spam", outgoing=True))
async def spam(event):
  id = event.chat_id
  raw = event.raw_text.split(" ")
  spamCount = raw[1]
  try:
    spamCount = int(spamCount)
  except:
    await event.edit("**ERROR OCCURRED \n Do :** ```.spam <number> | <spam Message>``` ")
    
  rawOp = event.raw_text.split("|")
  try:
    spamMessage = rawOp[1]
  except:
    await event.edit("**ERROR OCCURRED \n Do :** ```.spam <number> | <spam Message>``` ")
  i = 0
  while i != spamCount:
    await user.send_message(id,spamMessage)
    i = i+1
  print("\nCommand Used : spam \nLocation : {id} \n")
