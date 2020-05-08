# Reaction
import wikipedia
import random

wikipedia.set_lang('es')

with open('./data/rtas.txt', 'r') as f:
    insultos = f.read().splitlines()


def smartass(message):
    # change to for loop with try
    try:
        rta = wikipedia.summary(message, sentences=2, auto_suggest=True,
                                redirect=False).replace('\u200b','')

        if len(rta) > 500: # If msg too long, send first Paragraph
            rta = rta.partition('\n')[0] 
        return rta

    except Exception as e:
        print(e)
        print('no spanish')
        wikipedia.set_lang('en')

    # It won't reach this place unless exception (otherwise returns)
    try:
        rta = wikipedia.summary(message, sentences=2, auto_suggest=True,
                                redirect=False).replace('\u200b','')
        if len(rta) > 500:
            rta = rta.partition('\n')[0]

    except Exception as e:
        print(e)
        print('no english')
        rta = random.choice(insultos)

    finally:
        wikipedia.set_lang('es')
        return rta
