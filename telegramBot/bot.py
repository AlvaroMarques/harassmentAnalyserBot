import asyncio
import telegram


async def main():
    bot = telegram.Bot("5654110178:AAE_L4yjLkhwqbSZlNzt-NSg7z5QOOBSJS8")
    list = await bot.get_updates()
    for element in list:
        print(str(element.message['from']['id'])+':', element.message['text'])


if __name__ == '__main__':
    while(1):
        asyncio.run(main())
