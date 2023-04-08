import os
import openai
import json
from utils.voice_synthesizer import text_to_speech


openai.api_key = ""
model_id = "gpt-3.5-turbo"


def chatgpt_conversation(conversation_log):
    response = openai.ChatCompletion.create(model=model_id, messages=conversation_log)
    conversation_log.append(
        {
            "role": response.choices[0].message.role,
            "content": response.choices[0].message.content,
        }
    )

    return conversation_log


# System, assistant, user (System instigates the conversation)
conversation_log = []
conversation_log.append({"role": "system", "content": "Let's get started."})

conversation = chatgpt_conversation(conversation_log)

print(f"Role: {conversation[-1]['role']}, Message: {conversation[-1]['content']}")


while True:
    user_prompt = input("User Message: ")
    if user_prompt == "kill":
        break

    conversation_log.append({"role": "user", "content": user_prompt})
    print("\n\n")
    conversation = chatgpt_conversation(conversation_log)
    text_to_speech(conversation[-1]["content"])
    print("\n\n")
