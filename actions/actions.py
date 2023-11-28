from rasa_sdk import Action
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher
from typing import List, Dict, Text, Any

from gpt3_fallback import ActionGPT3Fallback

class ActionPlayVideo(Action):
    def name(self) -> str:
        return "action_play_video"

    def run(self, dispatcher: CollectingDispatcher,
            tracker, domain) -> List[Dict[Text, Any]]:
        # Custom logic to play video
        dispatcher.utter_message(text="Playing video now.")
        return []

class ActionPauseVideo(Action):
    def name(self) -> str:
        return "action_pause_video"

    def run(self, dispatcher: CollectingDispatcher,
            tracker, domain) -> List[Dict[Text, Any]]:
        # Custom logic to pause video
        dispatcher.utter_message(text="Pausing video.")
        return []

class ActionStopVideo(Action):
    def name(self) -> str:
        return "action_stop_video"

    def run(self, dispatcher: CollectingDispatcher,
            tracker, domain) -> List[Dict[Text, Any]]:
        # Custom logic to stop video
        dispatcher.utter_message(text="Stopping video.")
        return []

class ActionGPT3Fallback(Action):
    def name(self) -> str:
        return "action_gpt3_fallback"

   def run(self, dispatcher, tracker, domain):
        request = " ".join(tracker.latest_message['text'].split()[1:])
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=f"{request}",
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5,
        ).choices[0].text
        dispatcher.utter_message(text=response)
        return [SlotSet("request", request), SlotSet("response", response)]
