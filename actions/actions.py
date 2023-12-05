from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionPlayVideo(Action):
    def name(self) -> Text:
        return "action_play_video"

    async def run(self, dispatcher: CollectingDispatcher,
                  tracker: Tracker,
                  domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Add your logic here to play a video
        dispatcher.utter_message(text="Playing a video.")
        return []

class ActionPlaySpecificVideo(Action):
    def name(self) -> Text:
        return "action_play_specific_video"

    async def run(self, dispatcher: CollectingDispatcher,
                  tracker: Tracker,
                  domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Logic to play a specific video
        dispatcher.utter_message(text="Playing the specific video you requested.")
        return []

class ActionPlayVideosBySpecificArtist(Action):
    def name(self) -> Text:
        return "action_play_videos_by_specific_artist"

    async def run(self, dispatcher: CollectingDispatcher,
                  tracker: Tracker,
                  domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Logic for playing videos by a specific artist
        dispatcher.utter_message(text="Playing videos by the specified artist.")
        return []

class ActionPauseVideo(Action):
    def name(self) -> Text:
        return "action_pause_video"

    async def run(self, dispatcher: CollectingDispatcher,
                  tracker: Tracker,
                  domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Logic to pause the video
        dispatcher.utter_message(text="Video paused.")
        return []

class ActionResumeVideo(Action):
    def name(self) -> Text:
        return "action_resume_video"

    async def run(self, dispatcher: CollectingDispatcher,
                  tracker: Tracker,
                  domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Logic to resume the video
        dispatcher.utter_message(text="Resuming video.")
        return []

class ActionSkipVideo(Action):
    def name(self) -> Text:
        return "action_skip_video"

    async def run(self, dispatcher: CollectingDispatcher,
                  tracker: Tracker,
                  domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Logic to skip the video
        dispatcher.utter_message(text="Skipping to the next video.")
        return []

class ActionPreviousVideo(Action):
    def name(self) -> Text:
        return "action_previous_video"

    async def run(self, dispatcher: CollectingDispatcher,
                  tracker: Tracker,
                  domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Logic to play the previous video
        dispatcher.utter_message(text="Playing the previous video.")
        return []

class ActionAdjustVolumeVideo(Action):
    def name(self) -> Text:
        return "action_adjust_volume_video"

    async def run(self, dispatcher: CollectingDispatcher,
                  tracker: Tracker,
                  domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Logic to adjust the volume
        dispatcher.utter_message(text="Adjusting the volume of the video.")
        return []

class ActionSeekVideo(Action):
    def name(self) -> Text:
        return "action_seek_video"

    async def run(self, dispatcher: CollectingDispatcher,
                  tracker: Tracker,
                  domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Logic to seek within the video
        dispatcher.utter_message(text="Seeking to the specified point in the video.")
        return []

class ActionGPTFallback(Action):
    def name(self) -> Text:
        return "action_gpt_fallback"

    async def run(self, dispatcher: CollectingDispatcher,
                  tracker: Tracker,
                  domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Logic for handling out of scope queries
        dispatcher.utter_message(text="I'm not sure how to respond to that.")
        return []
