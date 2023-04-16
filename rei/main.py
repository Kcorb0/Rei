import os, sys
import openai
import json
from multiprocessing import process
from apps import time_tools
from utils.text_to_speech import text_to_speech
from utils.gpt_turbo import conversation


# Temporary usage loop, will be raplaced later for something practical.

WAKE_WORD = "Rei"


while True:
    listen = input("")

    if WAKE_WORD in listen:
        conversation()
    elif listen == "stop":
        break
