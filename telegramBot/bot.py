import asyncio
import telegram
import json

with open('messages.json', 'r') as openfile:
    # Reading from json file
    json_object = json.load(openfile)

async def main():
    # Start Bot
    bot = telegram.Bot("5654110178:AAE_L4yjLkhwqbSZlNzt-NSg7z5QOOBSJS8")
    # Get message list
    list = await bot.get_updates(offset=5)
    for element in list:
        if str(element.message['message_id']) not in json_object:
            # Analyze image 
            if element.message['text'] == None:
                # Get FIle
                file = await bot.get_file(element.message['photo'][2]['file_id'])

                # Register the image as received
                json_object[str(element.message['message_id'])] = "Image File"

                # Get image path and download it
                path = await file.download()
                
                # Request NSFW image detector APi
                import requests
                r = requests.post(
                    "https://api.deepai.org/api/nsfw-detector",
                    files={
                        'image': open(path, 'rb'),
                    },
                    headers={'api-key': 'quickstart-QUdJIGlzIGNvbWluZy4uLi4K'}
                )
                
                # Show result
                print(r.json())

            # Analyze text
            else:
                # Register the message as received
                json_object[str(element.message['message_id'])] = element.message['text']

                # Writing to json
                with open("messages.json", "w") as outfile:
                    outfile.write(json.dumps(json_object))
                print(json_object)


if __name__ == '__main__':
    while(1):
        asyncio.run(main())
