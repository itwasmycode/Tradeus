# actions.py

from currency_converter import CurrencyConverter

from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet
from rasa_core.channels import OutputChannel


class ActionCurrency(Action):
    def name (self):
        return 'action_currency'
    
    def run(self, dispatcher, tracker, domain):
        cur1 = tracker.get_slot('currency')
        cur2 = tracker.get_slot('currency_to')
        c_unit = int(tracker.get_slot('conversion_unit'))

        mapping = {cur1: 'USD', cur2: 'EUR'}
        cur1, cur2 = mapping.get(cur1), mapping.get(cur2)

        
        curr_obj = CurrencyConverter()
        converted_obj = curr_obj.convert(c_unit, cur1, cur2)


        dispatcher.utter_message(f"""It is just a {converted_obj}""")
        return [SlotSet('currency', cur1), SlotSet('currency_to', cur2), SlotSet('conversion_unit', c_unit)]
