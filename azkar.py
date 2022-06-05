import os
import subprocess
import threading
import time
import telegram
from telegram.ext import *
life = 0
telegram_api = " "  # Replace this with your telegram bot api
bot = telegram.Bot(token=telegram_api)

def start_command(update, context):
    update.message.reply_text("السلام عليكم و رحمه الله و بركاته , بوت الاذكار يهدف الى تذكيرك من حين الى اخر بذكر الله تقبل الله منا و منكم صالح الاعمال لتحديد وقت البوت اضغط على /time ")



def help_command(update, context):
    update.message.reply_text("Commands")


def handle_message(update, context):
    text = str(update.message.text).lower()
    r_text = responses(text)
    update.message.reply_text(r_text)

azkar = ["سبحان الله", "الحمد لله", "الله اكبر"]



def responses(input_text):
    user_message = str(input_text).lower()
    chat_id = bot.get_updates()[-1].message.chat_id

    if user_message == "/time":
        return "برجاء الرد علينا بالوقت المناسب و الفاصل بين كل ذكر و الاخر اختار بين 5 او 15 او 30 او 60 او 120 او 180 دقيقه , فقط اكتب الرقم بدون اى حروف مع اضافه / مثال /30"

    def zikr():

        if user_message == "/5":
            t = 1*5 
            for zikr in azkar:
                    bot.send_message(chat_id=chat_id, text=zikr)
                    time.sleep(t)              
    ##############################################################################
        if user_message == "/15":
            t = 1*10
            for zikr in azkar:
                    bot.send_message(chat_id=chat_id, text=zikr)
                    time.sleep(t)     

    ##############################################################################
        if user_message == "/30":
            t = 1*1800 
            for zikr in azkar:
                    bot.send_message(chat_id=chat_id, text=zikr)
                    time.sleep(t)          
    ##############################################################################
        if user_message == "/60":
            t = 60*60
            for zikr in azkar:
                    bot.send_message(chat_id=chat_id, text=zikr)
                    time.sleep(t)           
    ##############################################################################
        if user_message == "/120":
            t = 120*60 
            for zikr in azkar:
                    bot.send_message(chat_id=chat_id, text=zikr)
                    time.sleep(t)         
    ##############################################################################    
        if user_message == "/180":
            t = 180*60   
            for zikr in azkar:
                    bot.send_message(chat_id=chat_id, text=zikr)
                    time.sleep(t)    
   
    # t2 = threading.Thread(target=responses,args=(input_text))
    
    while life != 1:
        zikr()      


def error(update, context):
    print(f"Update {update} caused error {context.error}")


def main():
    updater = Updater(telegram_api, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("Start", start_command))
    dp.add_handler(CommandHandler("Help", help_command))
    dp.add_handler(MessageHandler(Filters.text, handle_message, pass_job_queue=True))
    dp.add_error_handler(error)
    updater.start_polling(0, timeout=10)
    updater.idle()


if __name__ == "__main__":
    print("Bot started.")
    main()
