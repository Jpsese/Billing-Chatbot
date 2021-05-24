class Parser:

    def __init__(self, event):
        self._id = event['from']['id']
        self._convoId = event['conversation']['id']
        self._serviceUrl = event['serviceUrl']
        self._type = event['type']
        if self._type == 'message':
            self._messagePayload = {
                'type': 'text',
                'value': event['text']
            }
        elif self._type == 'message_back':
            self._messagePayload = {
                'type': 'message_back',
                'value': event['text']
            }
        else:
            self._messagePayload = {'type': 'conversationUpdate', 'value': None}

    def __str__(self):
        return('FROM ID             : %s\n' \
               + 'CONVERSATION ID   : %s\n' \
               + 'SERVICE URL       : %s\n' \
               + 'MESSAGE TYPE      : %s\n' \
               + 'MESSAGE PAYLOAD   : %s\n')\
               % (self._id, self._convoId, self._serviceUrl, self._type, self._messagePayload)

    @property
    def id(self):
        return self._id

    @property
    def convoId(self):
        return self._convoId

    @property
    def serviceUrl(self):
        return self._serviceUrl

    @property
    def type(self):
        return self.type

    @property
    def messagePayload(self):
        return self._messagePayload

    @id.setter
    def id(self, id):
        self._id = id

    @convoId.setter
    def convoId(self, convoId):
        self._convoId = convoId

    @serviceUrl.setter
    def serviceUrl(self, serviceUrl):
        self._serviceUrl = serviceUrl

    @type.setter
    def type(self, type):
        self._type = type

    @messagePayload.setter
    def messagePayload(self, messagePayload):
        self._messagePayload = messagePayload

