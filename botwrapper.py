import requests

BASEURL = f'https://api.telegram.org/bot'

class TelegramBot:

    def __init__(self, botToken, chatID=None):
        self.baseURL = BASEURL 
        self.botToken = botToken
        self.chatID = chatID
        self.lastUpdateID = self.getLastUpdateID()
        self.defaultMessage = 'Desperté, cualquier cosa me avisan' 
        self.poolTime = None
        if self.chatID is not None:
            self.sendMessage(self.defaultMessage, self.chatID)
            

    def setChatID(chatID):
        self.chatID = chatID

    # ++++++ Basic Get Methods ++++++++++

    def getMe(self):
        try:
            r = requests.get(self.baseURL+self.botToken+'/getMe')
            return r.json()
        except Exception as e:
            print(e)
    
    def getUpdates(self, offset=None):
        url = self.baseURL+self.botToken+'/getUpdates'
        params = {'offset': offset}
        try:
            r = requests.get(url, params)
            return r.json()
        except Exception as e:
            print(e)

    def checkContent(self,r):
        return (r is not None) and r['ok'] and r['result']

    def getLastUpdateID(self):
        r = self.getUpdates()
        
        if self.checkContent(r):
            return r['result'][-1]['update_id']

    def getLastUpdates(self): # Before comming to existance it won't get anything
        if self.lastUpdateID is not None:
            offset = self.lastUpdateID + 1
        else:
            offset = None
            
        r = self.getUpdates(offset)
        
        if self.checkContent(r):
            self.lastUpdateID = r['result'][-1]['update_id']

        return r

    def whoAmI(self):
        pass

    def displayMyInfo(self):
        # print nicely resuls from getMe
        pass

    def getChatInfo(self, chatID=None):
        #Test
        chatID = chatID or self.chatID
        url = self.baseURL+self.botToken+'/getChat'
        params = {'chat_id': chatID}
        try:
            r = requests.get(url, params)
            return r.json()
        except Exception as e:
            print(e)
    
    # ++++++++ Basic POST methods ++++++++++++
    
    def sendMessage(self, message='test message', chatID=None):
        chatID = chatID or self.chatID
        url = self.baseURL+self.botToken+'/sendMessage'
        data = {'chat_id': chatID, 'text': message}
        try:
            r = requests.post(url, data)
            return r.json()
        except Exception as e:
            print(e)

    def sendLocalPhoto(self, photoPath, chatID=None):
        chatID = chatID or self.chatID
        url = self.baseURL+self.botToken+'/sendPhoto'
        file = { 'photo': open(photoPath, 'rb')}
        data = {'chat_id': chatID }
        try:
            r = requests.post(url, files=file, data=data)
            return r.json()
        except Exception as e:
            print(e)

    def sendRemotePhoto(self, photoUrl, chatID=None): #testear
        chatID = chatID or self.chatID
        url = self.baseURL+self.botToken+'/sendPhoto'
        data = {'chat_id': chatID, 'photo': photoUrl}
        try:
            r = requests.post(url, data)
            return r.json()
        except Exception as e:
            print(e)

    # ++++++++++ Others +++++++++++++++++++

    def respond(self, r, reaction):
        #r = self.getLastUpdates()
        
        if self.checkContent(r):

            for update in r['result']:
                try:
                    chatID = update['message']['chat']['id']
                    chatType = update['message']['chat']['type']
                    SenderID = update['message']['from']['id']
                    SenderName = update['message']['from']['first_name']
                    message = update['message']['text']

                except Exception as e:
                    print(e)
                    if 'chatID' in locals():
                        self.sendMessage(self.defaultMessage, chatID)

                else:
                    response = reaction(message)
                    if chatType != 'private':
                        response = SenderName+',\n'+response
                        
                    self.sendMessage(response, chatID)
