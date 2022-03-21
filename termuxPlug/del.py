□del□

#
@admin_cmd()
async def del(event):
  await toDel = event.get_reply_message()
  await toDel.delete()
  await event.delete()
