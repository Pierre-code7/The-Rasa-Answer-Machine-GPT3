# Import standard library packages
import logging
import os

# Import Rasa SDK components
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet, FollowupAction
from rasa_sdk.executor import CollectingDispatcher

# Import any additional modules your custom actions might need
import requests
import json

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# You can add any additional initialization code here

# Import your custom actions
from .actions import (ActionPlayVideo, ActionPlaySpecificVideo, ActionPlayVideosBySpecificArtist, 
                      ActionPauseVideo, ActionResumeVideo, ActionSkipVideo, ActionPreviousVideo, 
                      ActionAdjustVolumeVideo, ActionSeekVideo, ActionGPT3Fallback)

# Ensure that environment variables are loaded
if os.path.exists(".env"):
    from dotenv import load_dotenv
    load_dotenv()
