from TelegramBot.config import TOKEN, root_url_bot,url_Cur,USD
from TelegramBot.method import sendMessage, getUpdates
import requests

okCodes = (200,201)
def getAllRates():
    res = requests.get(url_Cur)
    if res.status_code in okCodes:
        result = res.json()
        return result
    else:
        print(f"Ошибка в запросе со статусом: {res.status_code}")

def exctractRate(rates, name):
    rate = None
    di = {'Approve': 0, 'Errore': 'не найдена данная валюта'}
    for i in rates:
        if i["Cur_Abbreviation"] in name:
             rate = i
    if rate:
        return rate
    else:
        return di

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
while True:
    res = getBotUpdates(TOKEN)
    last_update_id = res["result"][-1]["update_id"]
    if last_update_id > prev_update_id:
        chat_id = res["result"][-1]["message"]["chat"]["id"]
        last_update_text = res["result"][-1]["message"]["text"].upper()
        nameCurAll = last_update_text
        nameCur = []
        for i in nameCurAll.split():
            if len(i) == 3:
                nameCur.append(i)
        rates = getAllRates()
        result = exctractRate(rates, nameCur)
        if "Errore" in result:
            message = f"{result['Errore']}"
        else:
            message = f"Курс на сегодня {result['Date'][:10]} для {result['Cur_Abbreviation']} : {result['Cur_OfficialRate']}"
        sendMesage(message, chat_id)
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