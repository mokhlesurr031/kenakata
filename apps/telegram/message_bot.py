import requests

url = "https://api.telegram.org/bot6111218899%3AAAE-K0QPGJ1LruE_6fPynLpNqGsnzBP2rSE/sendMessage"

payload = {
    "text": {"data": "mahin"},
    "disable_web_page_preview": False,
    "disable_notification": False,
    "reply_to_message_id": None,
    "chat_id": "2036238925"
}
headers = {
    "accept": "application/json",
    "content-type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print(response.text)


# get chat if from "https://telegram-bot-sdk.readme.io/reference/getme" getUpdate

