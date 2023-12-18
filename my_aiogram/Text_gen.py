text = {
        446870226:"generated text"
        }

async def get_text(user):
    txt = text.get(user.id, None)
    if txt == None:
        raise Exception("No text for this user")
    return txt