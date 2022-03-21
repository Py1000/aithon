□ehi□

#
@admin_cmd()
async def ehi(event):
  id = event.chat_id
  rawMessage = event.raw_text.split(" ")
  try:
    try:
      e = rawMessage[1]
      eHiformat = f"""
{e}■■■{e}
{e}■■■{e}
 {e}{e}{e}{e}
{e}■■■{e}
{e}■■■{e}
"""
      await event.edit(eHiformat)
      print(f"\nCommand Used : ehi \nLocation : {id} \n")
    except:
      e = "😀"
      eHiformat = f"""
{e}■■■{e}
{e}■■■{e}
 {e}{e}{e}{e}
{e}■■■{e}
{e}■■■{e}
"""
      await event.edit(eHiformat)
      print(f"\nCommand Used : ehi \nLocation : {id} \n")
  except:
    await event.edit("**ERROR OCCURRED** \nDo: ```.ehi <emoji> ``` \n**OR** \nDo: ```.ehi```")
