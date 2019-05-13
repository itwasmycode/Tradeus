# pather.py
# This file contains All Directories. 

import os 

from enum import Enum


class Path(Enum):
    ROOT_FILE = os.getcwd()
    CONFIG_JSON_FILE = os.path.join(ROOT_FILE, "config_spacy.json")
    TRADE_NLU_FILE = os.path.join(ROOT_FILE, "models/nlu/default/tradenlu")
    MODEL_FILE = os.path.join(ROOT_FILE, "models/nlu")
    DATA_JSON_FILE = os.path.join(ROOT_FILE, "data/data.json")
    TRADE_DOMAIN = os.path.join(ROOT_FILE, "trade_domain.yml")
    STORIES = os.path.join(ROOT_FILE, "data/stories.md")
    DIALOGUE = os.path.join(ROOT_FILE,"models/dialogue")



