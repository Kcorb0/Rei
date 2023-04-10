import os, sys
from datetime import datetime
import openai
import json
from utils.voice_synthesizer import text_to_speech
from utils.gpt_turbo import conversation
from utils.time_options import get_time


# Temporary usage loop, will be raplaced later for something practical.

while True:
    choice = input("choice: ")  # Questions, utility

    if choice in ["kill", ""]:
        break
    elif choice == "Time":
        print(get_time())
        text_to_speech(f"It is, {get_time()}")
    elif choice == "Question":
        conversation()
