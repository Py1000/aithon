□rhi□

#
@admin_cmd()
async def rhi(event):
  id = event.chat_id
  rHiMessage = random.choice(rString)
  try:
    await event.edit(rHiMessage)
    print(f"\nCommand Used : rhi \nLocation : {id} \n")
  except:
    await event.edit("**ERROR OCCURRED**")
