# actions.py

from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from currency_converter import CurrencyConverter

from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet



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



class CommerceReceiver(Action):    
    def name(self):
        return 'action_checkout'
    
    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message('Done')



class ActionPostCheckout(Action):
    def name(self):
        return 'action_post_checkout'

    def run(self, dispatcher, tracker, domain):
        val = tracker.get_slot('product_id')
        dispatcher.utter_message(f"Just a thing with value {val}")
        return [SlotSet('product_id',val)]
