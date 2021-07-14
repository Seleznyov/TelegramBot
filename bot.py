from TelegramBot.config import TOKEN, root_url_bot,url_Cur,USD
from TelegramBot.method import sendMessage, getUpdates
import requests

okCodes = (200,201)
def allRates(name):
    res = requests.get(url_Cur)
    result = res.json()
    for i in result:
        if i["Cur_Abbreviation"] == name:
            return i["Cur_OfficialRate"]

allcurrenciesList = []
def allcurrencies():
    res = requests.get(url_Cur)
    result = res.json()
    for i in result:
        allcurrenciesList.append(i["Cur_Abbreviation"])

def getBotUpdates(token):
    res = requests.get(root_url_bot+token+getUpdates)
    if res.status_code in okCodes:
        result = res.json()
        return result
    else:
        print(f"Ошибка в запросе со статусом: {res.status_code}")

def sendMesage(mesage_text, id_chat):
    url = root_url_bot + TOKEN + sendMessage + "?" + "chat_id=" + str(id_chat) + "&" + "text=" + mesage_text
    res = requests.post(url)
    if res.status_code in okCodes:
        return True
    else:
        return False

prev_update_id = 0
allcurrencies()
while True:
    res = getBotUpdates(TOKEN)
    last_update_id = res["result"][-1]["update_id"]
    if last_update_id > prev_update_id:
        chat_id = res["result"][-1]["message"]["chat"]["id"]
        last_update_text = res["result"][-1]["message"]["text"]
        for nameCur in allcurrenciesList:
            if nameCur in last_update_text:
                message = nameCur
                sendMesage(str(allRates(message)), chat_id)
        # else:
        #     message = "sorry try again"
        #     sendMesage(message, chat_id)
    prev_update_id = last_update_id


# allRates("BGN")

res = getBotUpdates(TOKEN)
print(res)

# allcurrencies()
# print(allcurrenciesList)

# last_update_id = res["result"][-1]["message"]["text"]
# print(last_update_id)

# chat_id = res["result"][-1]["message"]["chat"]["id"]
# message = "xxx"
# sendMesage(message,chat_id)

# list=['AUD', 'AMD', 'BGN', 'UAH',
#       'DKK', 'USD', 'EUR', 'PLN', 'JPY',
#       'IRR', 'ISK', 'CAD', 'CNY', 'KWD',
#       'MDL', 'NZD', 'NOK', 'RUB', 'XDR', 'SGD',
#       'KGS', 'KZT', 'TRY', 'GBP', 'CZK', 'SEK', 'CHF']