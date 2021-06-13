from TelegramBot.config import TOKEN, root_url_bot,url_Cur,USD
from TelegramBot.method import sendMessage, getUpdates
import requests

# name = input("Введите валюту: Напрмер: Гривен или Доллар США или Евро ")
response_Cur = requests.get(url_Cur)
data_Cur = response_Cur.json()

res = requests.get(root_url_bot+TOKEN+getUpdates)
data_sms = res.json()

def CurrentRate(data_Cur,name):
    for i in data_Cur:
        if i["Cur_Name"] == name:
            print("Курс "+name+" равен "+str(i["Cur_OfficialRate"]))

def CurrentUSD(data_Cur,USD=USD):
    for i in data_Cur:
        if i["Cur_Name"] == USD:
            print("Курс "+USD+" равен "+str(i["Cur_OfficialRate"]))

def CurAbbreviation(data_Cur,Abbreviation):
    for i in data_Cur:
        if i["Cur_Abbreviation"] == Abbreviation:
            return "Курс "+Abbreviation+" равен "+str(i["Cur_OfficialRate"]) + " на " + i["Date"][:10]

def smsХai():
    for i in range(len(data_sms["result"])):
        if data_sms["result"][-1]["message"]["text"] == "/start":
            id_chat = data_sms["result"][-1]["message"]["chat"]["id"]
            requests.post(root_url_bot+TOKEN+sendMessage+"?"+"chat_id="+str(id_chat)+"&"+"text="+"XAI")
            break

def sendsmsCurRate():
    id_chat = data_sms["result"][-1]["message"]["chat"]["id"]
    last_test = data_sms["result"][-1]["message"]["text"]
    for i in data_Cur:
        if i["Cur_Abbreviation"] in last_test:
            # Cur_Abbreviation(data, i["Cur_Abbreviation"])
            requests.post(root_url_bot + TOKEN + sendMessage + "?" + "chat_id=" + str(id_chat) + "&" + "text=" +
                          CurAbbreviation(data_Cur, i["Cur_Abbreviation"]))


# Current_Rate(data,name)
# Current_USD(data)
smsХai()
sendsmsCurRate()
# GetUpdates()
# Cur_Abbreviation(data,"USD")
