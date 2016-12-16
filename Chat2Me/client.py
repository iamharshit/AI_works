from autobahn.twisted.websocket import WebSocketClientProtocol, \
    WebSocketClientFactory
#general settings
import speech_recognition as sr
import pyttsx
speech_engine = pyttsx.init('sapi5')
speech_engine.setProperty('rate', 110)
r = sr.Recognizer()
source = sr.Microphone()

class MyClientProtocol(WebSocketClientProtocol):

    def onConnect(self, response):
        print("Server connected: {0}".format(response.peer))

    def onOpen(self):
        #speech recognizer
        print("WebSocket connection open.")
        
        def hello():
            try:
                #audio = r.listen(source)    
                #speech = r.recognize_google(audio)
                speech = 'hello'
                print 'Human >> '+speech
                self.sendMessage(speech.encode('utf8'))
            except :
                speech = " "

        hello()

    def onMessage(self, payload, isBinary):
        #speak
        ans = payload.decode('utf8')
        print 'Bot Alive >> '+ans
	speech_engine.say(ans)
	speech_engine.runAndWait()

    def onClose(self, wasClean, code, reason):
        print("WebSocket connection closed: {0}".format(reason))


if __name__ == '__main__':

    import sys

    from twisted.python import log
    from twisted.internet import reactor

    log.startLogging(sys.stdout)

    factory = WebSocketClientFactory(u"ws://127.0.0.1:9000")
    factory.protocol = MyClientProtocol

    reactor.connectTCP("127.0.0.1", 9000, factory)
    reactor.run()
