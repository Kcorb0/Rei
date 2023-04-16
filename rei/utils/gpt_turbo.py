import os
import openai
import json
from utils.text_to_speech import text_to_speech

openai.api_key = json.load(open("rei/utils/configs/credentials.json"))["openai_api_key"]
model_id = "gpt-3.5-turbo"


def chatgpt_log(conversation_log):
    response = openai.ChatCompletion.create(model=model_id, messages=conversation_log)
    conversation_log.append(
        {
            "role": response.choices[0].message.role,
            "content": response.choices[0].message.content,
        }
    )

    return conversation_log


def conversation():
    conversation_log = []
    conversation_log.append({"role": "system", "content": "Let's get started."})

    conversation = chatgpt_log(conversation_log)

    print(f"Role: {conversation[-1]['role']}, Message: {conversation[-1]['content']}")

    # Temporary usage loop, will be raplaced later for something practical.

    while True:
        user_prompt = input("User Query: ")

        if user_prompt in ["kill", "stop", "end", "quit"]:
            break

        conversation_log.append({"role": "user", "content": user_prompt})
        conversation = chatgpt_log(conversation_log)
        text_to_speech(conversation[-1]["content"])
