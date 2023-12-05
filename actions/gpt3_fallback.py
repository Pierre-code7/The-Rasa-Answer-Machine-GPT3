import openai
import os
from dotenv import load_dotenv
from rasa_sdk import Action
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.interfaces import Tracker

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

class ActionGPT3Fallback(Action):
    def name(self) -> str:
        return "action_gpt3_fallback"
    
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: dict) -> list:
        # Extract the user's message, omitting the bot command if included
        user_message = " ".join(tracker.latest_message['text'].split()[1:])

        try:
            # Generate a response using OpenAI's GPT-3
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=f"{user_message}",
                max_tokens=1024,
                n=1,
                stop=None,
                temperature=0.5,
            ).choices[0].text.strip()

            # Send the response to the user
            dispatcher.utter_message(text=response)

            # Return slots to update (optional)
            return [SlotSet("request", user_message), SlotSet("response", response)]

        except Exception as e:
            # Handle exceptions like API errors
            dispatcher.utter_message(text="I'm sorry, I couldn't process your request.")
            print(f"GPT-3 API error: {e}")
            return []
