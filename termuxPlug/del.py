□del□

#
@admin_cmd()
async def del(event):
  id = event.chat_id
  try:
    toDel =  await event.get_reply_message()
    await toDel.delete()
    await event.delete()
    print(f"Command used : del \nLocation : {id}")
  except:
    event.edit("**ERROR OCCURRED** \nDo: ```.del <reply a message>```")
