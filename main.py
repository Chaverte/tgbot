import schedule
import telebot
from threading import Thread
from time import sleep
import random


photo = ("https://media.tenor.com/1Q_XcfZPDWsAAAAM/hump-day-funny.gif",
         "https://media.tenor.com/cUl2dOugXyMAAAAM/gm-coffee-time.gif",
         "https://media.tenor.com/aiZfUput5fsAAAAM/gutmornink-gudmorning.gif",
         "https://media.tenor.com/VNFjSuOEw4AAAAAM/good-morning-goodmorning.gif",
         "https://media.tenor.com/ICKb7sG6EOkAAAAM/great-day-have-a-great-day.gif")

TOKEN = "TOKEN"

bot = telebot.TeleBot('TOKEN')
some_id = -ID_KOM

def schedule_checker():
    while True:
        schedule.run_pending()
        sleep(1)

def function_to_run():
    return bot.send_animation(some_id, random.choice(photo))


if __name__ == "__main__":
    schedule.every().day.at("09:00").do(function_to_run)
    Thread(target=schedule_checker).start()