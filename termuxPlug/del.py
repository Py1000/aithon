□del□

#
@admin_cmd()
async def delOp(event):
  id = event.chat_id
  try:
    toDel =  await event.get_reply_message()
    await toDel.delete()
    await event.delete()
    print(f"\nCommand used : del \nLocation : {id} \n")
  except:
    await event.edit("**ERROR OCCURRED** \nDo: ```.del <reply a message>```")
