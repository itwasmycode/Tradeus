import os
import spacy
from pather import Path

spacy.load('en')

from rasa_nlu.training_data import load_data
from rasa_nlu import config
from rasa_nlu.model import Trainer, Metadata, Interpreter




class NluModel:
    # Constructed for being function seperated as private.
    def __init__(self, message)->None:
        self.message = message
        self.returner = self._run_nlu(message)
            
    
    @staticmethod
    def train_nlu(data_file: str = Path.DATA_JSON_FILE.value, config_file: str = Path.CONFIG_JSON_FILE.value, model_file : str = Path.MODEL_FILE.value)->None:
        training_data = load_data(data_file)
        trainer = Trainer(config.load(config_file))
        trainer.train(training_data)
        model_directory = trainer.persist(model_file, fixed_model_name = "tradenlu")

        
    def _run_nlu(self, message:str, trade_nlu_file=Path.TRADE_NLU_FILE.value)->str:
        interpreter = Interpreter.load(trade_nlu_file)
        return interpreter.parse(self.message)


print(NluModel("I want to buy your house").returner)

NluModel.train_nlu()
