from flask import Flask
from flask_socketio import SocketIO
import json


from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_core.policies.keras_policy import KerasPolicy
from rasa_core.policies.memoization import MemoizationPolicy
from rasa_core.utils import EndpointConfig
from rasa_core.channels.socketio import SocketIOInput

from rasa_core.interpreter import RegexInterpreter

from pather import Path

interpreter = RasaNLUInterpreter(Path.TRADE_NLU_FILE.value)
agent = Agent.load(Path.DIALOGUE.value, interpreter=interpreter)



input_channel = SocketIOInput(
	# event name for messages sent from the user
	user_message_evt="user_uttered",
	# event name for messages sent from the bot
	bot_message_evt="bot_uttered",
	# socket.io namespace to use for the messages
	namespace = None
)



s = agent.handle_channels([input_channel], 5004, serve_forever=True)


