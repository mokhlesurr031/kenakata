import telegram
import asyncio

async def send_telegram_message():
    bot = telegram.Bot(token='6111218899:AAE-K0QPGJ1LruE_6fPynLpNqGsnzBP2rSE')
    await bot.send_message(chat_id='2036238925', text={
        "name":"mahin",
        "contact": "",
    })


# define a function to call the async function
def main():
    asyncio.run(send_telegram_message())

# call the main function to run the async function
main()


# get chat if from "https://telegram-bot-sdk.readme.io/reference/getme" getUpdate

