imgs = {
        446870226:"https://i.ytimg.com/vi/_oSmhXeZbcY/maxresdefault.jpg"
        }

async def get_image(user):
    img = imgs.get(user.id, "https://i.ytimg.com/vi/_oSmhXeZbcY/maxresdefault.jpg")
    if img == None:
        raise Exception("No image for this user")
    return img