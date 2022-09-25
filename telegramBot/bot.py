import asyncio
import telegram
import json

with open('messages.json', 'r') as openfile:
    # Reading from json file
    json_object = json.load(openfile)

async def main():
    bot = telegram.Bot("5654110178:AAE_L4yjLkhwqbSZlNzt-NSg7z5QOOBSJS8")
    list = await bot.get_updates(offset=5)
    for element in list:
        if str(element.message['message_id']) not in json_object:
            json_object[str(element.message['message_id'])] = element.message['text']
            #print(str(element.message['from']['id'])+':', element.message['text'])
            # Writing to sample.json
            with open("messages.json", "w") as outfile:
                outfile.write(json.dumps(json_object))
            print(json_object)


if __name__ == '__main__':
    while(1):
        asyncio.run(main())
