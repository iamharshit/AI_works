## Chat2Me
Chat with a Bot.The Chatbot uses google API for Speech(S) to Text(T) and Text to Speech conversion.It uses AIML for text to text conversion, currently deployed on [super's](http://www.alicebot.org/superbot.html) AIML.The client specks at the client side where S->T happens and T goes to server where T->T happens and sends back to client which further converts T->S.The client in this case can either be a terminal or a webbrowser.

### Usage
* Run server: `python server.py`
* Run either of the client i.e client.html by `opening it with webbrowser` or client.py by `python client.py ws://127.0.0.1:9000`
* For client.html click on SEND button to send the text to server. 
