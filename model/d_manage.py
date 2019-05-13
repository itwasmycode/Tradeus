import logging
import rasa_core
from rasa_core.agent import Agent
from rasa_core.policies.keras_policy import KerasPolicy
from rasa_core.policies.memoization import MemoizationPolicy
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_core.utils import EndpointConfig
from rasa_core.run import serve_application
from rasa_core import config
from pather import Path



def train_dialogue(domain_file = Path.TRADE_DOMAIN.value,
					model_path = Path.DIALOGUE.value,
					training_data_file = Path.STORIES.value):				
	agent = Agent(domain_file, policies = [MemoizationPolicy(), KerasPolicy(max_history=3, epochs=200, batch_size=50)])
	data = agent.load_data(training_data_file) 
	agent.train(data)
				
	agent.persist(model_path)
	return agent



train_dialogue()