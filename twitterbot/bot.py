from config import getApi


api = getApi()

def postStatus(update):
    status = api.PostUpdate(update)
    print(status)

# tweets string
postStatus("my 5th tweet")

image = 'bot.jpg'

# tweet with image
def postWithImage(update):
    print(api.PostUpdate(update, media='bot.jpg'))
    
    
postWithImage("This is my profile picture again!")