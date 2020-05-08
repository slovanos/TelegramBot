### Telegram Bot ### 
import time
from parameters import PAUSE, BOTTOKEN, CHATID
from botwrapper import TelegramBot
from reaction import smartass

def main():
    print('Iniciando...')
    # Bot
    bot = TelegramBot(BOTTOKEN, CHATID)

    try:
        
        while True:
            r = bot.getLastUpdates()
            bot.respond(r,smartass)
            time.sleep(PAUSE)
            
    except KeyboardInterrupt:
        print('Stopped')


if __name__ == '__main__':
    main()
