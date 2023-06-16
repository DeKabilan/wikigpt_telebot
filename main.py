import telebot
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup
import time
from bs4 import BeautifulSoup as bs
import requests
sresults=[]
links=[]

bot = telebot.TeleBot("5983765325:AAHcQ33r6WuWrxYReZONwLkVQHZHOm2q4rw")

@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.send_message(message.chat.id,"Support the Dev: www.github.com/DeKabilan")



def results(link):
    url = requests.get(link)
    soup=bs(url.content,'lxml')
    results = soup.findAll('p')
    return results[1].text+"\n"+results[2].text



@bot.callback_query_handler(func=lambda message : True)
def callback_query(call):
    link = call.message.text
    if call.data == "0":
        curl=links[0]
        bot.send_message(call.message.chat.id,"-----"+sresults[0]+"-----"+"\n"+results(curl))
    if call.data == "1":
        curl=links[1]
        bot.send_message(call.message.chat.id,"-----"+sresults[1]+"-----"+"\n"+results(curl))
    if call.data == "2":
        curl=links[2]
        bot.send_message(call.message.chat.id,"------"+sresults[2]+"-----"+"\n"+results(curl))
    if call.data == "3":
        curl=links[3]
        bot.send_message(call.message.chat.id,"-----"+sresults[3]+"-----"+"\n"+results(curl))

def markup_inline():
    markup = InlineKeyboardMarkup()
    markup.width = 4
    markup.add(InlineKeyboardButton(sresults[0], callback_data="0"))
    markup.add(InlineKeyboardButton(sresults[1], callback_data="1"))
    markup.add(InlineKeyboardButton(sresults[2], callback_data="2"))
    markup.add(InlineKeyboardButton(sresults[3], callback_data="3"))
    return markup

def search(parameter):
    base='https://en.wikipedia.org'
    url = requests.get("https://en.wikipedia.org/w/index.php?search="+parameter+"&title=Special:Search&profile=advanced&fulltext=1&ns0=1")
    soup=bs(url.content,'lxml')
    search = soup.find('a',attrs={'data-serp-pos':'0'})
    sresults.append(search.text)
    links.append(base+search.get('href'))
    search = soup.find('a',attrs={'data-serp-pos':'1'})
    sresults.append(search.text)
    links.append(base+search.get('href'))
    search = soup.find('a',attrs={'data-serp-pos':'2'})
    sresults.append(search.text)
    links.append(base+search.get('href'))
    search = soup.find('a',attrs={'data-serp-pos':'3'})
    sresults.append(search.text)
    links.append(base+search.get('href'))

    

@bot.message_handler(func=lambda msg: msg)
def sendres(message):
    link=message.text
    sresults.clear()
    sresults.clear()
    search(link)
    bot.delete_message(message.chat.id,message.message_id)
    bot.send_message(message.chat.id,link,reply_markup= markup_inline())


while True:
    bot.polling()
    # try:
    #     bot.polling()
    # except Exception:
    #     print(Exception())
    #     time.sleep(5)